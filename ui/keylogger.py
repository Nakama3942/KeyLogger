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

import configparser
import pickle
import os
from pynput import keyboard, mouse

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,\
							QMainWindow,\
							QMessageBox,\
							QSystemTrayIcon,\
							QStyle,\
							QMenu
from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QIcon, QAction, QCloseEvent
from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_keylogger import Ui_KeyLogger
from src.color_scheme import schemes
from src.calendar import calendar

# todo Implement scrolling in ButtonManager with mouse.Listener
# todo Add more color schemes


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

	def terminate(self):
		self._keyboardListener.stop()
		self._mouseListener.stop()
		super().terminate()

	def _keyboard_click(self, key):
		try:
			self.keyboard_clicked.emit(str(key.name))
		except AttributeError:
			self.keyboard_clicked.emit(str(key))

	def _mouse_click(self, x, y, button, pressed):
		if pressed:
			self.mouse_clicked.emit(x, y, str(button.name))
		else:
			self.mouse_released.emit(x, y, str(button.name))


class KeyLogger(QMainWindow, Ui_KeyLogger):
	def __init__(self):
		super(KeyLogger, self).__init__()
		self.setupUi(self)

		# Icon initialization
		QDir.addSearchPath('icons', 'icons/')
		self.setWindowIcon(QIcon('icons:KeyLogger_Icon.png'))

		self.REBOOT: bool = False

		# Data (Color scheme)
		self.current_scheme = {}

		# It's a tracking of button clicks in the window
		self.toolTray.clicked.connect(self.toolTray_Clicked)
		self.checkMouseClick.stateChanged.connect(self.checkMouseClick_Changed)
		self.checkMouseRelease.stateChanged.connect(self.checkMouseRelease_Changed)
		self.comboScheme.currentIndexChanged.connect(self.comboScheme_CurrentIndexChanged)
		self.buttResetSettings.clicked.connect(self.buttResetSettings_Clicked)
		self.buttResetLogging.clicked.connect(self.buttResetLogging_Clicked)
		self.buttResetAll.clicked.connect(self.buttResetAll_Clicked)
		self.buttSaveLogging.clicked.connect(self.buttSaveLogging_Clicked)

		# Initialization of QSystemTrayIcon
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
		show_action = QAction("Show", self)
		show_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
		show_action.triggered.connect(self.tray_Show)
		output_action = QAction("Output to log", self)
		output_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
		output_action.triggered.connect(self.tray_Output)
		close_action = QAction("Close", self)
		close_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
		close_action.triggered.connect(self.tray_Close)
		tray_menu = QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(output_action)
		tray_menu.addAction(close_action)
		self.tray_icon.setContextMenu(tray_menu)

		self.toolTray.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))

		# Initialization of process of tracking
		self.button_manager = ButtonManager()
		self.button_manager.start()
		self.button_manager.keyboard_clicked.connect(self.keyboard_Clicked)
		self.button_manager.mouse_clicked.connect(self.mouse_Clicked)
		self.button_manager.mouse_released.connect(self.mouse_Released)

		# Data integrity check
		if not os.path.exists('data'):
			self.textBrowser.append(f"<span style='color: #{schemes[0]['other_data']};'>{calendar()} : The program is running for the first time... Configuration initialization:</span>")
			os.makedirs('data')
			self.saveData()
			self.textBrowser.append(f"<span style='color: #{schemes[0]['other_data']};'>{calendar()} : Configuration file created.</span>")
			self.textBrowser.append(f"<span style='color: #{schemes[0]['other_data']};'>{calendar()} : Program log created.</span>")
		else:
			try:
				self.textBrowser.append(f"<span style='color: #{schemes[0]['other_data']};'>{calendar()} : The program is running...</span>")
				# Reading settings
				config = configparser.ConfigParser()
				config.read("data/config.ini")
				self.checkKeyboardClick.setChecked(config.getboolean("Settings", "tracking_keyboard_click"))
				self.checkMouseClick.setChecked(config.getboolean("Settings", "tracking_mouse_click"))
				self.checkMouseClickCoord.setChecked(config.getboolean("Settings", "tracking_mouse_click_coord"))
				self.checkMouseRelease.setChecked(config.getboolean("Settings", "tracking_mouse_release"))
				self.checkMouseReleaseCoord.setChecked(config.getboolean("Settings", "tracking_mouse_release_coord"))
				self.comboScheme.setCurrentText(config.get("ColorScheme", "current_scheme"))
				# Reading program log
				with open("data/KeyLog.save", "rb") as save:
					self.textBrowser.setHtml(pickle.load(save))
			except configparser.NoSectionError:
				with open("data/KeyLog.save", "rb") as save:
					self.textBrowser.setHtml(pickle.load(save))
				self.saveData()
			except FileNotFoundError:
				self.saveData()

		# Checking if some settings can be displayed
		self.checkMouseClick_Changed()
		self.checkMouseRelease_Changed()
		self.comboScheme_CurrentIndexChanged()
		self.textBrowser.append(f"<span style='color: #{self.current_scheme['other_data']};'>{calendar()} : Start tracking...</span>")

	def tray_Show(self):
		self.tray_icon.hide()
		self.show()

	def tray_Output(self):
		self.buttSaveLogging_Clicked()
		os.startfile("key.log")

	def tray_Close(self):
		self.tray_Show()
		self.close()

	def toolTray_Clicked(self):
		self.tray_icon.show()
		self.hide()

	def checkMouseClick_Changed(self):
		if self.checkMouseClick.isChecked():
			self.checkMouseClickCoord.setEnabled(True)
		else:
			self.checkMouseClickCoord.setEnabled(False)

	def checkMouseRelease_Changed(self):
		if self.checkMouseRelease.isChecked():
			self.checkMouseReleaseCoord.setEnabled(True)
		else:
			self.checkMouseReleaseCoord.setEnabled(False)

	def comboScheme_CurrentIndexChanged(self):
		for item in schemes:
			if item['GUI'] == self.comboScheme.currentText():
				self.current_scheme['key_clicked'] = item['key_clicked']
				self.current_scheme['mouse_clicked'] = item['mouse_clicked']
				self.current_scheme['mouse_released'] = item['mouse_released']
				self.current_scheme['other_data'] = item['other_data']
				break

	def buttResetSettings_Clicked(self):
		self.textBrowser.append(f"<span style='color: #{self.current_scheme['other_data']};'>{calendar()} : Reboot tracking...</span>")
		self.button_manager.terminate()
		self.saveData()
		os.remove("data/config.ini")
		self.REBOOT = True
		self.close()

	def buttResetLogging_Clicked(self):
		self.button_manager.terminate()
		self.saveData()
		os.remove("data/KeyLog.save")
		self.REBOOT = True
		self.close()

	def buttResetAll_Clicked(self):
		self.button_manager.terminate()
		os.remove("data/config.ini")
		os.remove("data/KeyLog.save")
		os.rmdir("data")
		self.REBOOT = True
		self.close()

	def buttSaveLogging_Clicked(self):
		with open("key.log", "wt") as save:
			save.write(self.textBrowser.toPlainText())

	def keyboard_Clicked(self, key: str):
		if self.checkKeyboardClick.isChecked():
			self.textBrowser.append(f"<span style='color: #{self.current_scheme['key_clicked']};'>{calendar()} : Key pressed: {key}</span>")

	def mouse_Clicked(self, x: int, y: int, button: str):
		if self.checkMouseClick.isChecked():
			if self.checkMouseClickCoord.isChecked():
				self.textBrowser.append(f"<span style='color: #{self.current_scheme['mouse_clicked']};'>{calendar()} : Mouse clicked at ({x}, {y}) with {button}</span>")
			else:
				self.textBrowser.append(f"<span style='color: #{self.current_scheme['mouse_clicked']};'>{calendar()} : Mouse clicked with {button}</span>")

	def mouse_Released(self, x: int, y: int, button: str):
		if self.checkMouseRelease.isChecked():
			if self.checkMouseReleaseCoord.isChecked():
				self.textBrowser.append(f"<span style='color: #{self.current_scheme['mouse_released']};'>{calendar()} : Mouse released at ({x}, {y}) with {button}</span>")
			else:
				self.textBrowser.append(f"<span style='color: #{self.current_scheme['mouse_released']};'>{calendar()} : Mouse released with {button}</span>")

	def closeEvent(self, event: QCloseEvent):
		self.textBrowser.append(f"<span style='color: #{self.current_scheme['other_data']};'>{calendar()} : Stop tracking...</span>")
		self.button_manager.terminate()
		# Saving
		if not self.REBOOT:
			self.saveData()
		# Closing
		super().closeEvent(event)

	def saveData(self):
		# Saving data to a file, so you don't have to type it in every time
		config = configparser.ConfigParser()
		config.add_section('Settings')
		config.set('Settings', 'tracking_keyboard_click', str(self.checkKeyboardClick.isChecked()))
		config.set('Settings', 'tracking_mouse_click', str(self.checkMouseClick.isChecked()))
		config.set('Settings', 'tracking_mouse_click_coord', str(self.checkMouseClickCoord.isChecked()))
		config.set('Settings', 'tracking_mouse_release', str(self.checkMouseRelease.isChecked()))
		config.set('Settings', 'tracking_mouse_release_coord', str(self.checkMouseReleaseCoord.isChecked()))
		config.add_section('ColorScheme')
		config.set('ColorScheme', 'current_scheme', str(self.comboScheme.currentText()))
		with open('data/config.ini', 'w') as config_file:
			config.write(config_file)

		# Saving a log for a program
		with open("data/KeyLog.save", "wb") as save:
			pickle.dump(self.textBrowser.toHtml(), save)
