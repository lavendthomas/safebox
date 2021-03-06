# safeboxes_row.py
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

from .safeboxes_manager import SafeboxManger

from gi.repository import Gtk

import logging

@Gtk.Template(resource_path='/org/gnome/Safebox/safebox-row.ui')
class SafeboxRow(Gtk.ListBoxRow):
    __gtype_name__ = 'SafeboxRow'

    name_label = Gtk.Template.Child()
    mount_button = Gtk.Template.Child()
    status_label = Gtk.Template.Child()
    encrypted_location_label = Gtk.Template.Child()
    decrypted_location_label = Gtk.Template.Child()
    encryption_algorithm_label = Gtk.Template.Child()
    key_length_label = Gtk.Template.Child()
    edit_button = Gtk.Template.Child()
    delete_button = Gtk.Template.Child()

    def __init__(self, safebox_name: str):
        super().__init__()
        self.safebox_name = safebox_name

        self.handlers = {
            "toggle_revealer": self.toggle_revealer
        }

        self.builder = Gtk.Builder()
        self.builder.add_from_resource(
            "/org/gnome/Safebox/safebox-row.ui")
        self.builder.connect_signals(self.handlers)

        self.revealer = self.builder.get_object("revealer")
        self.row = self.builder.get_object("SafeboxRow")




    def toggle_revealer(self, source):
        self.revealer.set_reveal_child(not self.revealer.get_reveal_child())

        SafeboxManger.list_safeboxes()
