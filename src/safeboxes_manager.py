# safeboxes_manager.py
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

from .vaults_handler import DEFAULT_SAFEBOX_PATH, DEFAULT_VAULT_PATH
from os import listdir
import logging


class SafeboxManger:
    """
    Stores and makes accessible data around available safeboxes
    """

    def __init__(self):
        pass

    @staticmethod
    def list_safeboxes():

        folders = listdir(DEFAULT_SAFEBOX_PATH)
        logging.info(folders)



