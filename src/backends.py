# backends.py
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
import subprocess


class EncryptionBackend:

    def __init__(self):
        pass

    def mount(self, source: str, destination: str, password: str) -> bool:
        """
        :param source: the path of the folder that contained encrypted content
        :param destination: the path were the decrypted content should be stored
        :param password: the password used to store the content
        :returns True if the folder was successfully decrypted and mounted on the folder
        """
        pass

    def unmount(self):
        """
        Unmounts the folder containing the decrypted folder
        :returns: True if the decrypted folder was successfully decrypted
        """
        pass


ENCFS_PATH: str = "/usr/bin/encfs"      # TODO add in the flatpak
FUSERMOUNT_PATH: str = "/usr/bin/fusermount"


class Encfs(EncryptionBackend):

    def __init__(self):
        super().__init__()

    def mount(self, source, destination, password):
        new_env = os.environ.copy()

        args = [
            ENCFS_PATH,
            "-S",               # Read password from stdin
            "--standard",       # If creating a file system, use the default options
            source,
            destination
        ]

        process = subprocess.Popen(
            args=args,
            stdin=subprocess.PIPE if destination else None,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            env=new_env
        )

        logging.info(str(process.returncode))

        # something else than 'None' indicates that the process already terminated
        if not (process.returncode is None):
            pass

        def unmount(self):
            new_env = os.environ.copy()

            args = [
                FUSERMOUNT_PATH,
                "-u",
                destination
            ]

            process = subprocess.Popen(
                args=args,
                stdin=subprocess.PIPE if destination else None,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                env=new_env
            )

            logging.info(str(process.returncode))

            # something else than 'None' indicates that the process already terminated
            if not (process.returncode is None):
                pass