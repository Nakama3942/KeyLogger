# Form implementation generated from reading ui file 'KeyLogger.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_KeyLogger(object):
    def setupUi(self, KeyLogger):
        KeyLogger.setObjectName("KeyLogger")
        KeyLogger.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        KeyLogger.setFont(font)
        self.centralwidget = QtWidgets.QWidget(KeyLogger)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxSettings = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxSettings.setFont(font)
        self.groupBoxSettings.setObjectName("groupBoxSettings")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBoxSettings)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkKeyboardClick = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkKeyboardClick.setFont(font)
        self.checkKeyboardClick.setChecked(True)
        self.checkKeyboardClick.setObjectName("checkKeyboardClick")
        self.horizontalLayout_8.addWidget(self.checkKeyboardClick)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkMouseClick = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseClick.setFont(font)
        self.checkMouseClick.setChecked(True)
        self.checkMouseClick.setObjectName("checkMouseClick")
        self.horizontalLayout_2.addWidget(self.checkMouseClick)
        self.checkMouseClickCoord = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseClickCoord.setFont(font)
        self.checkMouseClickCoord.setChecked(True)
        self.checkMouseClickCoord.setObjectName("checkMouseClickCoord")
        self.horizontalLayout_2.addWidget(self.checkMouseClickCoord)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkMouseRelease = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseRelease.setFont(font)
        self.checkMouseRelease.setObjectName("checkMouseRelease")
        self.horizontalLayout_3.addWidget(self.checkMouseRelease)
        self.checkMouseReleaseCoord = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseReleaseCoord.setFont(font)
        self.checkMouseReleaseCoord.setChecked(True)
        self.checkMouseReleaseCoord.setObjectName("checkMouseReleaseCoord")
        self.horizontalLayout_3.addWidget(self.checkMouseReleaseCoord)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkMouseScroll = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseScroll.setFont(font)
        self.checkMouseScroll.setChecked(False)
        self.checkMouseScroll.setObjectName("checkMouseScroll")
        self.horizontalLayout_7.addWidget(self.checkMouseScroll)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.groupBoxSettings)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkMouseMove = QtWidgets.QCheckBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseMove.setFont(font)
        self.checkMouseMove.setObjectName("checkMouseMove")
        self.horizontalLayout_9.addWidget(self.checkMouseMove)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.groupBoxSettings)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.groupBoxColorScheme = QtWidgets.QGroupBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxColorScheme.setFont(font)
        self.groupBoxColorScheme.setObjectName("groupBoxColorScheme")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxColorScheme)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboScheme = QtWidgets.QComboBox(self.groupBoxColorScheme)
        self.comboScheme.setMinimumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboScheme.setFont(font)
        self.comboScheme.setObjectName("comboScheme")
        self.comboScheme.addItem("")
        self.comboScheme.addItem("")
        self.comboScheme.addItem("")
        self.verticalLayout_3.addWidget(self.comboScheme)
        self.horizontalLayout_5.addWidget(self.groupBoxColorScheme)
        self.horizontalLayout.addWidget(self.groupBoxSettings)
        self.groupBoxDiscard = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxDiscard.setFont(font)
        self.groupBoxDiscard.setObjectName("groupBoxDiscard")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxDiscard)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buttResetSettings = QtWidgets.QPushButton(self.groupBoxDiscard)
        self.buttResetSettings.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttResetSettings.setFont(font)
        self.buttResetSettings.setObjectName("buttResetSettings")
        self.verticalLayout_4.addWidget(self.buttResetSettings)
        self.buttResetLogging = QtWidgets.QPushButton(self.groupBoxDiscard)
        self.buttResetLogging.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttResetLogging.setFont(font)
        self.buttResetLogging.setObjectName("buttResetLogging")
        self.verticalLayout_4.addWidget(self.buttResetLogging)
        self.buttResetAll = QtWidgets.QPushButton(self.groupBoxDiscard)
        self.buttResetAll.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttResetAll.setFont(font)
        self.buttResetAll.setStyleSheet("color: red")
        self.buttResetAll.setObjectName("buttResetAll")
        self.verticalLayout_4.addWidget(self.buttResetAll)
        self.horizontalLayout.addWidget(self.groupBoxDiscard)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolTray = QtWidgets.QToolButton(self.centralwidget)
        self.toolTray.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolTray.setFont(font)
        self.toolTray.setText("")
        self.toolTray.setIconSize(QtCore.QSize(40, 40))
        self.toolTray.setObjectName("toolTray")
        self.horizontalLayout.addWidget(self.toolTray)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.groupBoxLoggingAction = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxLoggingAction.setFont(font)
        self.groupBoxLoggingAction.setObjectName("groupBoxLoggingAction")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxLoggingAction)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowserLoggingAction = QtWidgets.QTextBrowser(self.groupBoxLoggingAction)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowserLoggingAction.setFont(font)
        self.textBrowserLoggingAction.setObjectName("textBrowserLoggingAction")
        self.verticalLayout_2.addWidget(self.textBrowserLoggingAction)
        self.line_3 = QtWidgets.QFrame(self.groupBoxLoggingAction)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.buttSaveLoggingAction = QtWidgets.QPushButton(self.groupBoxLoggingAction)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttSaveLoggingAction.setFont(font)
        self.buttSaveLoggingAction.setObjectName("buttSaveLoggingAction")
        self.horizontalLayout_4.addWidget(self.buttSaveLoggingAction)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBoxLoggingAction)
        self.groupBoxLoggingMoving = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxLoggingMoving.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxLoggingMoving.setFont(font)
        self.groupBoxLoggingMoving.setObjectName("groupBoxLoggingMoving")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxLoggingMoving)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowserLoggingMoving = QtWidgets.QTextBrowser(self.groupBoxLoggingMoving)
        self.textBrowserLoggingMoving.setObjectName("textBrowserLoggingMoving")
        self.verticalLayout_5.addWidget(self.textBrowserLoggingMoving)
        self.line_4 = QtWidgets.QFrame(self.groupBoxLoggingMoving)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.buttSaveLoggingMoving = QtWidgets.QPushButton(self.groupBoxLoggingMoving)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttSaveLoggingMoving.setFont(font)
        self.buttSaveLoggingMoving.setObjectName("buttSaveLoggingMoving")
        self.horizontalLayout_10.addWidget(self.buttSaveLoggingMoving)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6.addWidget(self.groupBoxLoggingMoving)
        KeyLogger.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeyLogger)
        self.comboScheme.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(KeyLogger)

    def retranslateUi(self, KeyLogger):
        _translate = QtCore.QCoreApplication.translate
        KeyLogger.setWindowTitle(_translate("KeyLogger", "KEYLOGGER"))
        self.groupBoxSettings.setTitle(_translate("KeyLogger", "Settings"))
        self.checkKeyboardClick.setText(_translate("KeyLogger", "Clicking keyboard keystrokes"))
        self.checkMouseClick.setText(_translate("KeyLogger", "Clicking mouse keystrokes"))
        self.checkMouseClickCoord.setText(_translate("KeyLogger", "Track coordinates"))
        self.checkMouseRelease.setText(_translate("KeyLogger", "Releasing mouse keystrokes"))
        self.checkMouseReleaseCoord.setText(_translate("KeyLogger", "Track coordinates"))
        self.checkMouseScroll.setText(_translate("KeyLogger", "Scrolling mouse"))
        self.checkMouseMove.setText(_translate("KeyLogger", "Moving mouse"))
        self.groupBoxColorScheme.setTitle(_translate("KeyLogger", "Color Scheme"))
        self.comboScheme.setItemText(0, _translate("KeyLogger", "Standard"))
        self.comboScheme.setItemText(1, _translate("KeyLogger", "Monochrome"))
        self.comboScheme.setItemText(2, _translate("KeyLogger", "Sepia"))
        self.groupBoxDiscard.setTitle(_translate("KeyLogger", "Discard"))
        self.buttResetSettings.setText(_translate("KeyLogger", "Reset settings"))
        self.buttResetLogging.setText(_translate("KeyLogger", "Reset logging"))
        self.buttResetAll.setText(_translate("KeyLogger", "Reset All"))
        self.toolTray.setToolTip(_translate("KeyLogger", "Hide to tray"))
        self.groupBoxLoggingAction.setTitle(_translate("KeyLogger", "Logging action"))
        self.buttSaveLoggingAction.setText(_translate("KeyLogger", "Save user action logging"))
        self.groupBoxLoggingMoving.setTitle(_translate("KeyLogger", "Logging moving"))
        self.buttSaveLoggingMoving.setText(_translate("KeyLogger", "Save user moving logging"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KeyLogger = QtWidgets.QMainWindow()
    ui = Ui_KeyLogger()
    ui.setupUi(KeyLogger)
    KeyLogger.show()
    sys.exit(app.exec())
