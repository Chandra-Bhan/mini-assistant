# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvis_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1403, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -30, 1721, 1041))
        self.label.setMaximumSize(QtCore.QSize(1721, 1041))
        self.label.setSizeIncrement(QtCore.QSize(1721, 1041))
        self.label.setPixmap(QtGui.QPixmap("Jarvis Images/B.G/Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 0, 741, 501))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Jarvis Images/B.G/Iron_Template_1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-30, 370, 381, 261))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Jarvis Images/VoiceReg/Aqua.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 660, 361, 171))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Jarvis Images/ExtraGui/loading_1.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 401, 291))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Jarvis Images/ExtraGui/Earth_Template.gif"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(890, 540, 501, 291))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Jarvis Images/B.G/gyhf.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 580, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("font: 75 36pt \"Palatino Linotype\";\n"
"color: rgb(0, 85, 255);\n"
"background-color:transparent;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, -60, 681, 341))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Jarvis Images/ExtraGui/initial.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(950, 730, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAcceptDrops(True)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("font: 75 36pt \"Palatino Linotype\";\n"
"color: rgb(0, 85, 255);\n"
"background-color:transparent;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_3.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
