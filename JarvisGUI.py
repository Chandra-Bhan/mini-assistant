from jarvis_Ui import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
from Jarvis import ClapDetect

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui=Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_3.clicked.connect(self.close)


    def startFunc(self):
        self.jarvis_ui.movies_2=QtGui.QMovie("Jarvis Images/B.G/Iron_Template_1.gif")
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("Jarvis Images/VoiceReg/Aqua.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("Jarvis Images/ExtraGui/loading_1.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_5 = QtGui.QMovie("Jarvis Images/ExtraGui/Earth_Template.gif")
        self.jarvis_ui.label_5.setMovie(self.jarvis_ui.movies_5)
        self.jarvis_ui.movies_5.start()

        self.jarvis_ui.movies_7 = QtGui.QMovie("Jarvis Images/ExtraGui/initial.gif")
        self.jarvis_ui.label_7.setMovie(self.jarvis_ui.movies_7)
        self.jarvis_ui.movies_7.start()
        print("Jarvis has been started")


#Jarvis.ClapDetect()
Gui_App=QApplication(sys.argv)
Gui_jarvis=Gui_Start()
Gui_jarvis.show()

exit(Gui_App.exec_())
