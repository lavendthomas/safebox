# window.py
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

from gi.repository import Gtk, GLib
from .vaults_handler import Vault
from .safebox_row import SafeboxRow
from .safebox_group import SafeboxGroup
import os

@Gtk.Template(resource_path='/org/gnome/Safebox/window.ui')
class SafeboxWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'SafeboxWindow'


    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.handlers = {
            "onDestroy": Gtk.main_quit,
            "on_mount_button_clicked": self._on_mount_button_clicked,
            "on_lets_get_started": self.on_lets_get_started,
            "on_first_safebox_add_button_clicked": self.on_first_safebox_add_button_clicked,
            "on_first_safebox_i_understand_button_clicked": self.on_first_safebox_i_understand_button_clicked
        }

        self.builder = Gtk.Builder()
        self.builder.add_from_resource(
            "/org/gnome/Safebox/window.ui")
        self.builder.connect_signals(self.handlers)

        window = self.builder.get_object("SafeboxWindow")
        window.show_all()

    def on_lets_get_started(self, source):
        first_safebox_stack: Gtk.Stack = self.builder.get_object("first_safebox_stack")
        choice_box = self.builder.get_object("first_safebox_name_choice_box")
        first_safebox_stack.set_visible_child(choice_box)

    def on_first_safebox_add_button_clicked(self, source):

        name_entry: Gtk.Entry = self.builder.get_object("first_safebox_name_entry")
        pass_entry: Gtk.Entry = self.builder.get_object("first_safebox_password_entry")

        name = name_entry.get_text()
        password = pass_entry.get_text()

        logging.info(name + " " + password)

        first_safebox_stack: Gtk.Stack = self.builder.get_object("first_safebox_stack")
        warning_box = self.builder.get_object("first_safebox_warning_box")
        first_safebox_stack.set_visible_child(warning_box)

    def on_first_safebox_i_understand_button_clicked(self, source):

        dummy_row = SafeboxRow("test")
        dummy_group = SafeboxGroup("Mounted")
        # dummy_row.row.connect("clicked", dummy_row.toggle_revealer)

        dummy_group.group.pack_start(dummy_row.row, True, True, 0)

        safeboxes_list_viewport = self.builder.get_object("safeboxes_list_viewport")
        safeboxes_list_viewport.add(dummy_group.group)

        safeboxes_stack = self.builder.get_object("safeboxes_stack")
        safeboxes_stack.set_visible_child(safeboxes_list_viewport)

        safeboxes_stack.show_all()
        safeboxes_list_viewport.show_all()
        dummy_row.show_all()

        logging.info("Visible" + str(safeboxes_stack.get_visible_child().get_children()))

    def _on_mount_button_clicked(self, source):
        logging.info("Hello World!")

        v = Vault("test", True)
        v.create()
        # v.mount()
        # v.unmount()



