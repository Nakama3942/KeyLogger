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
from src.printer import Printer


# This class is a QThread that responds to user interaction with keyboard keys and the mouse
class ButtonManager(QThread):
	keyboard_clicked = pyqtSignal(str)
	mouse_clicked = pyqtSignal(int, int, str)
	mouse_released = pyqtSignal(int, int, str)
	mouse_move = pyqtSignal(int, int)
	mouse_scroll = pyqtSignal(int, int, int, int)

	def __init__(self):
		"""
		The function __init__() is a constructor for the class ButtonManager. It calls the constructor of the superclass (the
		class it inherits from) and then creates two listeners, one for the keyboard and one for the mouse
		"""
		super(ButtonManager, self).__init__()
		self._keyboardListener = keyboard.Listener(on_press=self._keyboard_click)
		self._mouseListener = mouse.Listener(on_move=self._mouse_move, on_click=self._mouse_click, on_scroll=self._mouse_scroll)

	def run(self):
		"""
		The function starts the keyboard and mouse listeners
		"""
		self._keyboardListener.start()
		self._mouseListener.start()

	def terminate(self):
		"""
		It stops the keyboard and mouse listeners, and then calls the terminate function of the super class
		"""
		self._keyboardListener.stop()
		self._mouseListener.stop()
		super().terminate()

	def _keyboard_click(self, key):
		"""
		It emits a signal that is connected to a slot in the main window

		:param key: The key that was pressed
		"""
		try:
			self.keyboard_clicked.emit(str(key.name))
		except AttributeError:
			self.keyboard_clicked.emit(str(key))

	def _mouse_move(self, x, y):
		"""
		It emits a signal that tells the main thread to move the mouse

		:param x: The x coordinate of the mouse cursor
		:param y: The y coordinate of the mouse cursor, relative to the top-left corner of the screen
		"""
		# todo Slow down
		self.mouse_move.emit(x, y)

	def _mouse_click(self, x, y, button, pressed):
		"""
		If the mouse button is pressed, emit a signal with the x and y coordinates of the mouse and the name of the button

		:param x: The x coordinate of the mouse click
		:param y: The y coordinate of the mouse event
		:param button: The mouse button that was clicked
		:param pressed: True if the button was pressed, False if it was released
		"""
		if pressed:
			self.mouse_clicked.emit(x, y, str(button.name))
		else:
			self.mouse_released.emit(x, y, str(button.name))

	def _mouse_scroll(self, x, y, dx, dy):
		"""
		It emits a signal when the mouse is scrolled

		:param x: The x position of the mouse cursor
		:param y: The y-coordinate of the mouse cursor, relative to the window
		:param dx: The amount scrolled horizontally, expressed in integer units
		:param dy: The amount of scrolling that was done. Positive values indicate that the mouse wheel was rotated forward,
		away from the user; negative values indicate that the mouse wheel was rotated backward, toward the user
		"""
		self.mouse_scroll.emit(x, y, dx, dy)


class KeyLogger(QMainWindow, Ui_KeyLogger):
	def __init__(self):
		super(KeyLogger, self).__init__()
		self.setupUi(self)

		# Icon initialization
		QDir.addSearchPath('icons', 'icons/')
		self.setWindowIcon(QIcon('icons:KeyLogger_Icon.png'))

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())

		# Reboot flag
		self.REBOOT: bool = False

		# Data (Color scheme and strings)
		self.current_scheme = {}
		self.printer = Printer(schemes[0])

		# It's a tracking of button clicks in the window
		self.toolTray.clicked.connect(self.toolTray_Clicked)
		self.checkMouseClick.stateChanged.connect(self.checkMouseClick_Changed)
		self.checkMouseRelease.stateChanged.connect(self.checkMouseRelease_Changed)
		self.checkMouseMove.stateChanged.connect(self.checkMouseMove_Changed)
		self.comboScheme.currentTextChanged.connect(self.comboScheme_CurrentIndexChanged)
		self.buttResetSettings.clicked.connect(self.buttResetSettings_Clicked)
		self.buttResetLogging.clicked.connect(self.buttResetLogging_Clicked)
		self.buttResetAll.clicked.connect(self.buttResetAll_Clicked)
		self.buttSaveLoggingAction.clicked.connect(self.buttSaveLoggingAction_Clicked)
		self.buttSaveLoggingMoving.clicked.connect(self.buttSaveLoggingMoving_Clicked)

		# Initialization of QSystemTrayIcon
		self.toolTray.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
		show_action = QAction("Show", self)
		show_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
		show_action.triggered.connect(self.tray_Show)
		output_action = QAction("Output action to log", self)
		output_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
		output_action.triggered.connect(self.tray_ActionOutput)
		output_moving = QAction("Output moving to log", self)
		output_moving.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
		output_moving.triggered.connect(self.tray_MovingOutput)
		close_action = QAction("Close", self)
		close_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
		close_action.triggered.connect(self.tray_Close)
		tray_menu = QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(output_action)
		tray_menu.addAction(output_moving)
		tray_menu.addAction(close_action)
		self.tray_icon.setContextMenu(tray_menu)

		# Initialization of process of tracking
		self.button_manager = ButtonManager()
		self.button_manager.start()
		self.button_manager.keyboard_clicked.connect(self.keyboard_Clicked)
		self.button_manager.mouse_clicked.connect(self.mouse_Clicked)
		self.button_manager.mouse_released.connect(self.mouse_Released)
		self.button_manager.mouse_move.connect(self.mouse_Move)
		self.button_manager.mouse_scroll.connect(self.mouse_Scroll)

		# Data integrity check
		if not os.path.exists('data'):
			self.textBrowserLoggingAction.append(self.printer.init_string())
			os.makedirs('data')
			self.saveData()
			self.textBrowserLoggingAction.append(self.printer.config_string())
			self.textBrowserLoggingAction.append(self.printer.log_created_string())
		else:
			try:
				self.textBrowserLoggingAction.append(self.printer.run_string())
				# Reading settings
				config = configparser.ConfigParser()
				config.read("data/config.ini")
				self.checkKeyboardClick.setChecked(config.getboolean("Settings", "tracking_keyboard_click"))
				self.checkMouseClick.setChecked(config.getboolean("Settings", "tracking_mouse_click"))
				self.checkMouseClickCoord.setChecked(config.getboolean("Settings", "tracking_mouse_click_coord"))
				self.checkMouseRelease.setChecked(config.getboolean("Settings", "tracking_mouse_release"))
				self.checkMouseReleaseCoord.setChecked(config.getboolean("Settings", "tracking_mouse_release_coord"))
				self.checkMouseScroll.setChecked(config.getboolean("Settings", "tracking_mouse_scroll"))
				self.checkMouseMove.setChecked(config.getboolean("Settings", "tracking_mouse_move"))
				self.comboScheme.setCurrentText(config.get("ColorScheme", "current_scheme"))
				# Reading program log
				with open("data/KeyLog.save", "rb") as save:
					data = pickle.load(save)
					self.textBrowserLoggingAction.setHtml(data[0])
					self.textBrowserLoggingMoving.setHtml(data[1])
			except configparser.NoSectionError:
				# Reading program log
				with open("data/KeyLog.save", "rb") as save:
					data = pickle.load(save)
					self.textBrowserLoggingAction.setHtml(data[0])
					self.textBrowserLoggingMoving.setHtml(data[1])
				# Creating the necessary files through saving
				self.saveData()
			except FileNotFoundError:
				# Creating the necessary files through saving
				self.saveData()

		# Checking if some settings can be displayed
		self.checkMouseClick_Changed()
		self.checkMouseRelease_Changed()
		self.comboScheme_CurrentIndexChanged(self.comboScheme.currentText(), False)
		self.textBrowserLoggingAction.append(self.printer.start_track_string())

	def tray_Show(self):
		"""
		The function hides the tray icon, shows the main window, and prints a message to the text browser
		"""
		self.tray_icon.hide()
		self.show()
		self.textBrowserLoggingAction.append(self.printer.show_program_string())

	def tray_ActionOutput(self):
		"""
		It saves actions the log file, then opens it
		"""
		self.buttSaveLoggingAction_Clicked()
		os.startfile("key.log")

	def tray_MovingOutput(self):
		"""
		It saves moving the log file, then opens it
		"""
		self.buttSaveLoggingMoving_Clicked()
		os.startfile("mov.log")

	def tray_Close(self):
		"""
		It closes the program
		"""
		self.tray_Show()
		self.close()

	def toolTray_Clicked(self):
		"""
		The function hides the program and shows the tray icon
		"""
		self.tray_icon.show()
		self.hide()
		self.textBrowserLoggingAction.append(self.printer.hide_program_string())

	def checkMouseClick_Changed(self):
		"""
		If the checkbox is checked, enable the other checkbox. If it's not checked, disable the other checkbox
		"""
		if self.checkMouseClick.isChecked():
			self.checkMouseClickCoord.setEnabled(True)
		else:
			self.checkMouseClickCoord.setEnabled(False)

	def checkMouseRelease_Changed(self):
		"""
		If the checkbox is checked, enable the other checkbox. If it's not checked, disable the other checkbox
		"""
		if self.checkMouseRelease.isChecked():
			self.checkMouseReleaseCoord.setEnabled(True)
		else:
			self.checkMouseReleaseCoord.setEnabled(False)

	def checkMouseMove_Changed(self):
		"""
		If the checkbox is checked, then start tracking mouse movement. If the checkbox is unchecked, then stop tracking mouse
		movement
		"""
		if self.checkMouseMove.isChecked():
			self.textBrowserLoggingMoving.append(self.printer.start_track_moving_string())
		else:
			self.textBrowserLoggingMoving.append(self.printer.stop_track_moving_string())

	def comboScheme_CurrentIndexChanged(self, new_color_scheme: str, changed: bool = True):
		"""
		It takes a string as an argument, and then it loops through a list of dictionaries, and if the string matches the value
		of the key 'SCHEME_NAME' in the dictionary, it sets the value of the key 'SCHEME_NAME' in the dictionary
		'current_scheme' to the value of the key 'SCHEME_NAME' in the dictionary that was found in the list of dictionaries

		:param new_color_scheme: The name of the color scheme that was selected
		:type new_color_scheme: str
		:param changed: bool = True, defaults to True
		:type changed: bool (optional)
		"""
		for item in schemes:
			if item['SCHEME_NAME'] == new_color_scheme:
				self.current_scheme['SCHEME_NAME'] = item['SCHEME_NAME']
				self.current_scheme['processing_data'] = item['processing_data']
				self.current_scheme['hide_show'] = item['hide_show']
				self.current_scheme['color_scheme_change'] = item['color_scheme_change']
				self.current_scheme['reboot'] = item['reboot']
				self.current_scheme['export'] = item['export']
				self.current_scheme['key_pressed'] = item['key_pressed']
				self.current_scheme['mouse_clicked'] = item['mouse_clicked']
				self.current_scheme['mouse_clicked_coord'] = item['mouse_clicked_coord']
				self.current_scheme['mouse_released'] = item['mouse_released']
				self.current_scheme['mouse_released_coord'] = item['mouse_released_coord']
				self.current_scheme['mouse_scrolled'] = item['mouse_scrolled']
				self.current_scheme['mouse_scrolled_coord'] = item['mouse_scrolled_coord']
				self.current_scheme['moving_tracking'] = item['moving_tracking']
				self.current_scheme['mouse_moved'] = item['mouse_moved']
				self.current_scheme['mouse_moved_coord'] = item['mouse_moved_coord']

				self.printer.reinit(self.current_scheme)
				if changed:
					self.textBrowserLoggingAction.append(self.printer.change_scheme_string())
				break

	def buttResetSettings_Clicked(self):
		"""
		It resets the settings to default and reboots the program
		"""
		self.textBrowserLoggingAction.append(self.printer.reboot_tracking_string())
		self.button_manager.terminate()
		self.saveData()
		os.remove("data/config.ini")
		self.REBOOT = True
		self.close()

	def buttResetLogging_Clicked(self):
		"""
		It resets the logging and reboots the program
		"""
		self.button_manager.terminate()
		self.saveData()
		os.remove("data/KeyLog.save")
		self.REBOOT = True
		self.close()

	def buttResetAll_Clicked(self):
		"""
		It deletes the config file, the keylogger file, and the data directory
		"""
		self.button_manager.terminate()
		os.remove("data/config.ini")
		os.remove("data/KeyLog.save")
		os.rmdir("data")
		self.REBOOT = True
		self.close()

	def buttSaveLoggingAction_Clicked(self):
		"""
		It opens a file called key.log and writes the contents of the textBrowserLoggingAction widget to it
		"""
		with open("key.log", "wt") as save:
			save.write(self.textBrowserLoggingAction.toPlainText())
			self.textBrowserLoggingAction.append(self.printer.export_action_string())

	def buttSaveLoggingMoving_Clicked(self):
		"""
		It opens a file called mov.log and writes the contents of the textBrowserLoggingMoving widget to it
		"""
		with open("mov.log", "wt") as save:
			save.write(self.textBrowserLoggingMoving.toPlainText())
			self.textBrowserLoggingAction.append(self.printer.export_moving_string())

	def keyboard_Clicked(self, key: str):
		"""
		Sends the pressed keyboard key to the printer

		:param key: keyboard keystroke
		:type key: str
		"""
		if self.checkKeyboardClick.isChecked():
			self.textBrowserLoggingAction.append(self.printer.key_pressed_string(key))

	def mouse_Clicked(self, x: int, y: int, button: str):
		"""
		If the checkbox is checked, then if the other checkbox is checked, then print the mouse click with coordinates,
		otherwise print the mouse click without coordinates

		:param x: the x coordinate of the mouse click
		:type x: int
		:param y: the y coordinate of the mouse click
		:type y: int
		:param button: mouse keystroke
		:type button: str
		"""
		if self.checkMouseClick.isChecked():
			if self.checkMouseClickCoord.isChecked():
				self.textBrowserLoggingAction.append(self.printer.mouse_click_coord_string(x, y, button))
			else:
				self.textBrowserLoggingAction.append(self.printer.mouse_click_string(button))

	def mouse_Released(self, x: int, y: int, button: str):
		"""
		The function checks if the checkbox is checked, and if it is, it checks if the checkbox for coordinates is checked, and
		if it is, it prints the coordinates, otherwise it prints the button

		:param x: the x coordinate of the mouse
		:type x: int
		:param y: the y coordinate of the mouse
		:type y: int
		:param button: mouse keystroke
		:type button: str
		"""
		if self.checkMouseRelease.isChecked():
			if self.checkMouseReleaseCoord.isChecked():
				self.textBrowserLoggingAction.append(self.printer.mouse_release_coord_string(x, y, button))
			else:
				self.textBrowserLoggingAction.append(self.printer.mouse_release_string(button))

	def mouse_Move(self, x: int, y: int):
		"""
		If the checkbox is checked, then append the mouse move string to the text browser

		:param x: the x coordinate of the mouse
		:type x: int
		:param y: the y coordinate of the mouse
		:type y: int
		"""
		if self.checkMouseMove.isChecked():
			self.textBrowserLoggingMoving.append(self.printer.mouse_move_string(x, y))

	def mouse_Scroll(self, x: int, y: int, dx: int, dy: int):
		"""
		It prints the mouse scroll action to the textBrowserLoggingAction

		:param x: the x position of the mouse cursor
		:type x: int
		:param y: the x position of the mouse cursor
		:type y: int
		:param dx: the amount scrolled horizontally, expressed in multiples of the WHEEL_DELTA constant. A positive value
		indicates that the wheel was rotated to the right
		:type dx: int
		:param dy: the vertical scroll amount. Positive values indicate that the mouse wheel was rotated forward, away from the
		user; negative values indicate that the mouse wheel was rotated backward, toward the user
		:type dy: int
		"""
		if self.checkMouseScroll.isChecked():
			self.textBrowserLoggingAction.append(self.printer.mouse_scroll_string(x, y, dx, dy))

	def closeEvent(self, event: QCloseEvent):
		"""
		The function is called when the user closes the GUI. It stops the printer, saves the data, and closes the GUI

		:param event: close event
		:type event: QCloseEvent
		"""
		self.textBrowserLoggingAction.append(self.printer.stop_track_string())
		self.button_manager.terminate()
		# Saving
		if not self.REBOOT:
			self.saveData()
		# Closing
		super().closeEvent(event)

	def saveData(self):
		"""
		The function saves the data from the GUI to a file, so you don't have to type it in every time
		"""
		# Saving data to a file, so you don't have to type it in every time
		config = configparser.ConfigParser()
		config.add_section('Settings')
		config.set('Settings', 'tracking_keyboard_click', str(self.checkKeyboardClick.isChecked()))
		config.set('Settings', 'tracking_mouse_click', str(self.checkMouseClick.isChecked()))
		config.set('Settings', 'tracking_mouse_click_coord', str(self.checkMouseClickCoord.isChecked()))
		config.set('Settings', 'tracking_mouse_release', str(self.checkMouseRelease.isChecked()))
		config.set('Settings', 'tracking_mouse_release_coord', str(self.checkMouseReleaseCoord.isChecked()))
		config.set('Settings', 'tracking_mouse_scroll', str(self.checkMouseScroll.isChecked()))
		config.set('Settings', 'tracking_mouse_move', str(self.checkMouseMove.isChecked()))
		config.add_section('ColorScheme')
		config.set('ColorScheme', 'current_scheme', str(self.comboScheme.currentText()))
		with open('data/config.ini', 'w') as config_file:
			config.write(config_file)

		# Saving a log for a program
		with open("data/KeyLog.save", "wb") as save:
			data = [self.textBrowserLoggingAction.toHtml(), self.textBrowserLoggingMoving.toHtml()]
			pickle.dump(data, save)
