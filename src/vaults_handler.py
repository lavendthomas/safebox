# vaults_handler.py
#
# Copyright 2020 Thomas Lavend'Homme
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import logging
import os

from .backends import Encfs, EncryptionBackend

from gi.repository import Gio, GLib

DEFAULT_SAFEBOX_PATH = os.path.join(GLib.get_user_data_dir(), "safebox")
DEFAULT_VAULT_PATH = os.path.join(GLib.get_user_data_dir(), "safebox", "vaults")


class Vault:

    def __init__(self, name: str, password: str, is_internal: bool = True, custom_path: str = None):
        """
            :param is_internal: if the content of the folder is contained within the app's data
        """
        self.name: str = name
        self.is_internal: bool = is_internal
        self.state = None
        self.password = password

        if self.is_internal:
            self.encrypted_directory: str = os.path.join(DEFAULT_VAULT_PATH, name)
        else:
            self.encrypted_directory: str = custom_path

        self.mounted_directory = os.path.join(GLib.get_home_dir(), "Bureau", "safetest")

    """
    Creates or verify that the folder containing the encrypted data is existant and initialised
    """
    def create(self):
        """
        Initialises the folder containing the encrypted version of the data.
        Creates the folder and initialises the encypted folder
        """

        # Create all necessary folders
        safebox_folder: Gio.File = Gio.File.new_for_path(DEFAULT_SAFEBOX_PATH)
        vaults_folder: Gio.File = Gio.File.new_for_path(DEFAULT_VAULT_PATH)
        encrypted_directory: Gio.File = Gio.File.new_for_path(self.encrypted_directory)
        mounted_dir: Gio.File = Gio.File.new_for_path(self.mounted_directory)

        for _directory in [safebox_folder,
                           vaults_folder,
                           encrypted_directory,
                           mounted_dir]:

            if _directory.query_exists():
                logging.info(self.encrypted_directory + " exists.")
            else:
                logging.info(self.encrypted_directory + " does not exist, creating it...")
                _directory.make_directory()
                logging.info("Done.")
            del _directory

        encryption: EncryptionBackend = Encfs()

        encryption.init(self.encrypted_directory,
                        self.mounted_directory,
                        "pass")

    def destroy(self):
        """
        Deletes the folder containing all of the encrypted data
        """
        pass

    def mount(self):
        encryption: EncryptionBackend = Encfs()
        success = encryption.mount(self.encrypted_directory,
                                   self.mounted_directory,
                                   "pass")

        logging.info("Sucessfully mounted: ", success)

    def unmount(self):
        encryption: EncryptionBackend = Encfs
        success = encryption.unmount(encryption)
        logging.info("Unmounting successful")

