from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QApplication)
from termcolor import colored
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text=colored('red',attrs=['reverse','blink'])
        
        ##titulo da janela##
        self.setWindowTitle('CALCULADORA')
        self.setFixedSize(QSize(700,500))
        self.setStyleSheet('background-color: gray;')
        
        self.input_janela=QLabel(self)
        self.input_janela.setGeometry(60,30,400,60)
        self.input_janela.setText(colored('numeros','red',attrs=['reverse','blink']))
        self.input_janela.setStyleSheet('border: 1px solid black;')
        
        self.button_1=QPushButton(self)
        self.button_1.setGeometry(60,120,70,60)
        self.button_1.setText('1')
        self.button_1.clicked.connect(self.numero_1)
        
        self.button_2=QPushButton(self)
        self.button_2.setGeometry(130,120,70,60)
        self.button_2.setText('2')
        self.button_2.clicked.connect(self.numero_2)
        
    def numero_1(self):
        self.input_janela.setText('1')
        

    def numero_2(self):
        self.input_janela.setText('2')
        
        
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()
        