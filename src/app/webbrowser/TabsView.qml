/*
 * Copyright 2014 Canonical Ltd.
 *
 * This file is part of webbrowser-app.
 *
 * webbrowser-app is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 3.
 *
 * webbrowser-app is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0
import Ubuntu.Components 0.1

Item {
    id: tabsview

    property alias model: listview.model

    signal newTabRequested()
    signal done()

    Rectangle {
        anchors.fill: parent
        color: "#312f2c"
    }

    ListView {
        id: listview

        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
            bottom: toolbar.top
        }

        spacing: units.gu(-10)

        delegate: TabPreview {
            width: parent.width
            height: units.gu(40)

            title: model.title ? model.title : model.url
            webview: model.webview

            onSelected: {
                tabsview.model.currentIndex = index
                tabsview.done()
            }
            onCloseRequested: {
                var webview = tabsview.model.remove(index)
                if (webview) {
                    webview.destroy()
                }
                if (tabsview.model.count === 0) {
                    tabsview.newTabRequested()
                    tabsview.done()
                }
            }
        }
    }

    Item {
        id: toolbar

        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        height: units.gu(7)

        Rectangle {
            anchors.fill: parent
            color: "#312f2c"
            opacity: 0.8
        }

        Button {
            anchors {
                left: parent.left
                leftMargin: units.gu(2)
                verticalCenter: parent.verticalCenter
            }

            color: "#312f2c"

            text: i18n.tr("Done")

            onClicked: tabsview.done()
        }

        ToolbarButton {
            anchors {
                right: parent.right
                rightMargin: units.gu(2)
                verticalCenter: parent.verticalCenter
            }
            height: parent.height - units.gu(2)
            width: height

            text: i18n.tr("Add")

            iconName: "add"

            onTriggered: {
                tabsview.newTabRequested()
                tabsview.done()
            }

            MouseArea {
                // XXX: for some reason the parent button’s triggered() signal is never emitted?
                anchors.fill: parent
                onClicked: parent.trigger()
            }
        }
    }
}
