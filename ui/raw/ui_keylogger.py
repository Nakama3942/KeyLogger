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
        KeyLogger.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        KeyLogger.setFont(font)
        self.centralwidget = QtWidgets.QWidget(KeyLogger)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkKeyboardClick = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkKeyboardClick.setFont(font)
        self.checkKeyboardClick.setChecked(True)
        self.checkKeyboardClick.setObjectName("checkKeyboardClick")
        self.verticalLayout.addWidget(self.checkKeyboardClick)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkMouseClick = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseClick.setFont(font)
        self.checkMouseClick.setChecked(True)
        self.checkMouseClick.setObjectName("checkMouseClick")
        self.horizontalLayout_2.addWidget(self.checkMouseClick)
        self.checkMouseClickCoord = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseClickCoord.setFont(font)
        self.checkMouseClickCoord.setChecked(True)
        self.checkMouseClickCoord.setObjectName("checkMouseClickCoord")
        self.horizontalLayout_2.addWidget(self.checkMouseClickCoord)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkMouseRelease = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseRelease.setFont(font)
        self.checkMouseRelease.setObjectName("checkMouseRelease")
        self.horizontalLayout_3.addWidget(self.checkMouseRelease)
        self.checkMouseReleaseCoord = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkMouseReleaseCoord.setFont(font)
        self.checkMouseReleaseCoord.setChecked(True)
        self.checkMouseReleaseCoord.setObjectName("checkMouseReleaseCoord")
        self.horizontalLayout_3.addWidget(self.checkMouseReleaseCoord)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboScheme = QtWidgets.QComboBox(self.groupBox_2)
        self.comboScheme.setMinimumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboScheme.setFont(font)
        self.comboScheme.setObjectName("comboScheme")
        self.comboScheme.addItem("")
        self.comboScheme.addItem("")
        self.comboScheme.addItem("")
        self.verticalLayout_3.addWidget(self.comboScheme)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buttResetSettings = QtWidgets.QPushButton(self.groupBox_3)
        self.buttResetSettings.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttResetSettings.setFont(font)
        self.buttResetSettings.setObjectName("buttResetSettings")
        self.verticalLayout_4.addWidget(self.buttResetSettings)
        self.buttResetLogging = QtWidgets.QPushButton(self.groupBox_3)
        self.buttResetLogging.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttResetLogging.setFont(font)
        self.buttResetLogging.setObjectName("buttResetLogging")
        self.verticalLayout_4.addWidget(self.buttResetLogging)
        self.buttResetAll = QtWidgets.QPushButton(self.groupBox_3)
        self.buttResetAll.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttResetAll.setFont(font)
        self.buttResetAll.setStyleSheet("color: red")
        self.buttResetAll.setObjectName("buttResetAll")
        self.verticalLayout_4.addWidget(self.buttResetAll)
        self.horizontalLayout.addWidget(self.groupBox_3)
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
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.buttSaveLogging = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttSaveLogging.setFont(font)
        self.buttSaveLogging.setObjectName("buttSaveLogging")
        self.horizontalLayout_4.addWidget(self.buttSaveLogging)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        KeyLogger.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeyLogger)
        self.comboScheme.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(KeyLogger)

    def retranslateUi(self, KeyLogger):
        _translate = QtCore.QCoreApplication.translate
        KeyLogger.setWindowTitle(_translate("KeyLogger", "KEYLOGGER"))
        self.groupBox.setTitle(_translate("KeyLogger", "Settings"))
        self.checkKeyboardClick.setText(_translate("KeyLogger", "Clicking keyboard keystrokes"))
        self.checkMouseClick.setText(_translate("KeyLogger", "Clicking mouse keystrokes"))
        self.checkMouseClickCoord.setText(_translate("KeyLogger", "Track coordinates"))
        self.checkMouseRelease.setText(_translate("KeyLogger", "Releasing mouse keystrokes"))
        self.checkMouseReleaseCoord.setText(_translate("KeyLogger", "Track coordinates"))
        self.groupBox_2.setTitle(_translate("KeyLogger", "Color Scheme"))
        self.comboScheme.setItemText(0, _translate("KeyLogger", "Standard"))
        self.comboScheme.setItemText(1, _translate("KeyLogger", "Monochrome"))
        self.comboScheme.setItemText(2, _translate("KeyLogger", "Sepia"))
        self.groupBox_3.setTitle(_translate("KeyLogger", "Discard"))
        self.buttResetSettings.setText(_translate("KeyLogger", "Reset settings"))
        self.buttResetLogging.setText(_translate("KeyLogger", "Reset logging"))
        self.buttResetAll.setText(_translate("KeyLogger", "Reset All"))
        self.toolTray.setToolTip(_translate("KeyLogger", "Hide to tray"))
        self.groupBox_4.setTitle(_translate("KeyLogger", "Logging"))
        self.buttSaveLogging.setText(_translate("KeyLogger", "Save user logging"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KeyLogger = QtWidgets.QMainWindow()
    ui = Ui_KeyLogger()
    ui.setupUi(KeyLogger)
    KeyLogger.show()
    sys.exit(app.exec())
