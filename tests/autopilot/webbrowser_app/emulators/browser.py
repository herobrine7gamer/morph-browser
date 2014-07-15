# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#
# Copyright 2013-2014 Canonical
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from ubuntuuitoolkit import emulators as uitk


class Selection(uitk.UbuntuUIToolkitEmulatorBase):

    def get_rectangle(self):
        return self.select_single("QQuickItem", objectName="rectangle")

    def get_handle(self, name):
        return self.select_single("SelectionHandle", objectName=name)


class TabPreview(uitk.UbuntuUIToolkitEmulatorBase):

    def get_close_button(self):
        return self.select_single("AbstractButton", objectName="closeButton")


class TabsView(uitk.UbuntuUIToolkitEmulatorBase):

    def get_previews(self):
        return self.select_many(TabPreview)

    def get_ordered_previews(self):
        previews = self.get_previews()
        previews.sort(key=lambda tab: tab.y)
        return previews

    def get_done_button(self):
        return self.select_single("Button", objectName="doneButton")

    def get_add_button(self):
        return self.select_single("ToolbarAction", objectName="addTabButton")


class Browser(uitk.MainView):

    """
    An emulator class that makes it easy to interact with the webbrowser app.
    """

    def get_window(self):
        return self.get_parent()

    def get_keyboard_rectangle(self):
        return self.select_single("KeyboardRectangle")

    def get_chrome(self):
        return self.select_single("Chrome")

    def get_address_bar(self):
        return self.select_single("AddressBar")

    def get_address_bar_clear_button(self):
        textfield = self.get_address_bar_text_field()
        return textfield.select_single("AbstractButton")

    def get_address_bar_action_button(self):
        textfield = self.get_address_bar_text_field()
        return textfield.select_single("QQuickMouseArea",
                                       objectName="actionButton")

    def get_back_button(self):
        return self.select_single("ChromeButton", objectName="backButton")

    def get_forward_button(self):
        return self.select_single("ChromeButton", objectName="forwardButton")

    def get_drawer_button(self):
        return self.select_single("ChromeButton", objectName="drawerButton")

    def get_current_webview(self):
        return self.select_single("WebViewImpl", current=True)

    def get_visible_webviews(self):
        return self.select_many("WebViewImpl", visible=True)

    def get_error_sheet(self):
        return self.select_single("ErrorSheet")

    def get_address_bar_text_field(self):
        return self.get_address_bar().select_single("TextField")

    def get_address_bar_suggestions(self):
        return self.select_single("Suggestions")

    def get_address_bar_suggestions_listview(self):
        suggestions = self.get_address_bar_suggestions()
        return suggestions.select_single("QQuickListView")

    def get_address_bar_suggestions_listview_entries(self):
        listview = self.get_address_bar_suggestions_listview()
        return listview.select_many("Base")

    def get_geolocation_dialog(self):
        return self.wait_select_single("GeolocationPermissionRequest")

    def get_selection(self):
        return self.wait_select_single(Selection)

    def get_selection_actions(self):
        return self.wait_select_single("ActionSelectionPopover",
                                       objectName="selectionActions")

    def get_drawer(self):
        return self.wait_select_single("QQuickItem", objectName="drawer",
                                       clip=False)

    def get_drawer_action(self, actionName):
        drawer = self.get_drawer()
        return drawer.select_single("AbstractButton", objectName=actionName)

    def get_tabs_view(self):
        return self.wait_select_single(TabsView)

    def get_new_tab_view(self):
        return self.wait_select_single("NewTabView")
