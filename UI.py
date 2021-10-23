import sys
from PyQt5 import QtTest, QtWidgets, QtCore
from PyQt5.QtWidgets import * 

from Project import Ui_MainWindow

class GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.gu = Ui_MainWindow()
        self.gu.setupUi(self)

app = QApplication(sys.argv)
window = GUI()
window.show()
sys.exit(app.exec_())
