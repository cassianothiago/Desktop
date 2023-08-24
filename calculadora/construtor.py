from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QApplication)
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ##titulo da janela##
        self.setWindowTitle('CALCULADORA')
        self.setFixedSize(QSize(300,450))
        self.setStyleSheet('background-color: gray;')
        
        self.input_janela=QLabel(self)
        self.input_janela.setGeometry(60,30,200,60)
        self.input_janela.setText('numeros')
        self.input_janela.setStyleSheet('border: 1px solid black;')
        
        self.button_1=QPushButton(self)
        self.button_1.setGeometry(60,120,70,60)
        self.button_1.setText('1')
        self.button_1.clicked.connect(self.numero_1)
        
        self.button_2=QPushButton(self)
        self.button_2.setGeometry(130,120,70,60)
        self.button_2.setText('2')
        self.button_2.clicked.connect(self.numero_2)
        
        self.button_3=QPushButton(self)
        self.button_3.setGeometry(200,120,70,60)
        self.button_3.setText('3')
        self.button_3.clicked.connect(self.numero_3)
        
        self.button_4=QPushButton(self)
        self.button_4.setGeometry(60,180,70,60)
        self.button_4.setText('4')
        self.button_4.clicked.connect(self.numero_4)
        
        self.button_5=QPushButton(self)
        self.button_5.setGeometry(130,180,70,60)
        self.button_5.setText('5')
        self.button_5.clicked.connect(self.numero_5)
        
        self.button_6=QPushButton(self)
        self.button_6.setGeometry(200,180,70,60)
        self.button_6.setText('6')
        self.button_6.clicked.connect(self.numero_6)
        
        self.button_7=QPushButton(self)
        self.button_7.setGeometry(60,240,70,60)
        self.button_7.setText('7')
        self.button_7.clicked.connect(self.numero_7)
        
        self.button_8=QPushButton(self)
        self.button_8.setGeometry(130,240,70,60)
        self.button_8.setText('8')
        self.button_8.clicked.connect(self.numero_8)
        
        self.button_9=QPushButton(self)
        self.button_9.setGeometry(130,240,70,60)
        self.button_9.setText('9')
        self.button_9.clicked.connect(self.numero_9)
        
    def numero_1(self):
        self.input_janela.setText('1')
        
    def numero_2(self):
        self.input_janela.setText('2')
        
    def numero_3(self):
        self.input_janela.setText('3')
    
    def numero_4(self):
        self.input_janela.setText('4')
    
    def numero_5(self):
        self.input_janela.setText('5')
        
    def numero_6(self):
        self.input_janela.setText('6')
    
    def numero_7(self):
        self.input_janela.setText('7')
    
    def numero_8(self):
        self.input_janela.setText('8')
    
    def numero_8(self):
        self.input_janela.setText('9')
        
        
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()
        