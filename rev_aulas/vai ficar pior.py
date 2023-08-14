import sys
from typing import Optional

import PySide6.QtCore 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap,Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vai ficar pior')
        self.label=QLabel('oi mundo')
        #self.label.setAlignment(Qt.AlignmentFlag())
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()