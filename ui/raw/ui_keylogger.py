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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolTray = QtWidgets.QToolButton(self.centralwidget)
        self.toolTray.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolTray.setFont(font)
        self.toolTray.setObjectName("toolTray")
        self.horizontalLayout.addWidget(self.toolTray)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        KeyLogger.setCentralWidget(self.centralwidget)

        self.retranslateUi(KeyLogger)
        QtCore.QMetaObject.connectSlotsByName(KeyLogger)

    def retranslateUi(self, KeyLogger):
        _translate = QtCore.QCoreApplication.translate
        KeyLogger.setWindowTitle(_translate("KeyLogger", "KEYLOGGER"))
        self.toolTray.setText(_translate("KeyLogger", "Tray"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KeyLogger = QtWidgets.QMainWindow()
    ui = Ui_KeyLogger()
    ui.setupUi(KeyLogger)
    KeyLogger.show()
    sys.exit(app.exec())