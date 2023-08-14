import sys
from typing import Optional

import PySide6.QtCore 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap,Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exercio entreque n 2')
        self.button=QPushButton('botão',self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.imprimir)
        self.resultado=QLabel(self)
        self.resultado.setGeometry(10,150,280,30)
        self.digitar=QLineEdit(self)
        self.digitar.setGeometry(100,10,80,30)
        
    def imprimir(self):
        numero=int(self.digitar.text())
        if numero % 2==0:
            self.resultado.setText('par')
        else:
            self.resultado.setText('impar')
            
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()