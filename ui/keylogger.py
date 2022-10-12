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
import datetime
# import pickle
# import os
from pynput import keyboard, mouse

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,\
                            QMainWindow,\
                            QMessageBox,\
                            QSystemTrayIcon,\
                            QStyle,\
                            QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_keylogger import Ui_KeyLogger


class ButtonManager(QThread):
    keyboard_clicked = pyqtSignal(str)
    mouse_clicked = pyqtSignal(int, int, str)
    mouse_released = pyqtSignal(int, int, str)

    def __init__(self):
        super(ButtonManager, self).__init__()
        self._keyboardListener = keyboard.Listener(on_press=self._keyboard_click)
        self._mouseListener = mouse.Listener(on_click=self._mouse_click)

    def run(self):
        self._keyboardListener.start()
        self._mouseListener.start()

    def _keyboard_click(self, key):
        try:
            self.keyboard_clicked.emit(str(key.name))
        except AttributeError:
            self.keyboard_clicked.emit(str(key))

    def _mouse_click(self, x, y, button, pressed):
        if pressed:
            self.mouse_clicked.emit(x, y, str(button))
        else:
            self.mouse_released.emit(x, y, str(button))


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

        self.button_manager = ButtonManager()
        self.button_manager.start()
        self.button_manager.keyboard_clicked.connect(self.keyboard_Clicked)
        self.button_manager.mouse_clicked.connect(self.mouse_Clicked)
        self.button_manager.mouse_released.connect(self.mouse_Released)

    def tray_Show(self):
        self.tray_icon.hide()
        self.show()

    def toolTray_Clicked(self):
        self.tray_icon.show()
        self.hide()

    def keyboard_Clicked(self, key: str):
        self.textBrowser.append(f'{datetime.datetime.now()} Key pressed: {key}')

    def mouse_Clicked(self, x: int, y: int, button: str):
        self.textBrowser.append(f'{datetime.datetime.now()} Mouse clicked at ({x}, {y}) with {button}')

    def mouse_Released(self, x: int, y: int, button: str):
        self.textBrowser.append(f'{datetime.datetime.now()} Mouse released at ({x}, {y}) with {button}')
