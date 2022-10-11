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

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,\
                            QMainWindow,\
                            QMessageBox,\
                            QSystemTrayIcon,\
                            QStyle,\
                            QMenu
# from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QAction
# from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_keylogger import Ui_KeyLogger


# This class is a QThread that runs a function that tests a port to see if it's open
# class PortTestThread(QThread):
#     attempt = pyqtSignal(bool, str, int)
#
#     def __init__(self, host: str, port: int):
#         super(PortTestThread, self).__init__()
#         self.host: str = host
#         self.port: int = port
#
#     def run(self):
#         """
#         It attempts to connect to a host on a given port, and it emits a signal with result to connect, the host and port
#         number
#         """
#         s = socket.socket()
#         try:
#             s.connect((self.host, self.port))  # Connection attempt
#             # s.settimeout(0.2)  # Timeout for a little more speed
#         except:
#             self.attempt.emit(False, self.host, self.port)  # Port is closed
#         else:
#             self.attempt.emit(True, self.host, self.port)  # Port is opened


class KeyLogger(QMainWindow, Ui_KeyLogger):
    def __init__(self):
        super(KeyLogger, self).__init__()
        self.setupUi(self)

        # It's a tracking of button clicks in the window
        self.toolTray.clicked.connect(self.toolTray_Clicked)
        # self.linePorts.textChanged.connect(self.buttScan_Active)
        # self.toolClear.clicked.connect(self.toolClear_Clicked)
        # self.buttSave.clicked.connect(self.buttSave_Clicked)
        # self.buttOpen.clicked.connect(self.buttOpen_Clicked)
        # self.toolDelete.clicked.connect(self.toolDelete_Clicked)
        # self.toolStop.clicked.connect(self.toolStop_Clicked)

        # инициализировать QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        # self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))

        '''
              Определите и добавьте шаги для работы со значком в системном трее
            show - show window
            hide - hide window
            exit - exit from application
        '''
        show_action = QAction("Show", self)
        show_action.triggered.connect(self.tray_Show)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        self.tray_icon.setContextMenu(tray_menu)
        # self.tray_icon.show()

    def tray_Show(self):
        self.tray_icon.hide()
        self.show()

    def toolTray_Clicked(self):
        self.tray_icon.show()
        self.hide()
