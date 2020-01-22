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

import os

from gi.repository import Gio, GLib

DEFAULT_VAULT_PATH = os.path.join(GLib.get_user_data_dir(), "vaults")


class Vault:

    """
    :param is_internal: if the content of the folder is contained within the app's data
    """
    def __init__(self, name: str, is_internal: bool, custom_path: str = None):
        self.name: str = name
        self.is_internal: bool = is_internal
        self.status = None

        if self.is_internal:
            self.directory: str = os.path.join(DEFAULT_VAULT_PATH, name)
        else:
            self.directory: str = custom_path

    """
    Creates or verify that the folder containing the encrypted data is existant and initialised
    """
    def create(self):
        # Create DEFAULT_VAULT_PATH folder
        vaults_folder: Gio.File = Gio.File.new_for_path(DEFAULT_VAULT_PATH)
        if not vaults_folder.query_exists():
            vaults_folder.make_directory()
        del vaults_folder

        directory: Gio.File = Gio.File.new_for_path(self.directory)
        if directory.query_exists():
            print(self.directory + " exists")
        else:
            print(self.directory + " does not exist, creating it...")
            directory.make_directory()
            print("Done.")
        pass

    def mount(self):
        pass

    def unmount(self):
        pass

