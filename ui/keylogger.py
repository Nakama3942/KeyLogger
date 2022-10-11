#  Copyright © 2022 Kalynovsky Valentin. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# import socket
# from threading import Thread
# from time import sleep
# import pickle
# import os

# import PyQt6
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,\
                            QMainWindow,\
                            QMessageBox,\
                            QSystemTrayIcon,\
                            QStyle,\
                            QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeyEvent
# from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_keylogger import Ui_KeyLogger


class KeyLogger(QMainWindow, Ui_KeyLogger):
    def __init__(self):
        super(KeyLogger, self).__init__()
        self.setupUi(self)

        # It's a tracking of button clicks in the window
        self.toolTray.clicked.connect(self.toolTray_Clicked)

        # Initialization of QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
        show_action = QAction("Show", self)
        show_action.triggered.connect(self.tray_Show)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        self.tray_icon.setContextMenu(tray_menu)

    def tray_Show(self):
        self.tray_icon.hide()
        self.show()

    def toolTray_Clicked(self):
        self.tray_icon.show()
        self.hide()

    def keyPressEvent(self, event: QKeyEvent):
        for item in Qt.Key:
            if event.key() == item:
                self.textBrowser.append(str(item))
                break
