from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, 
QLineEdit)
from PySide6.QtGui import QPixmap

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('CALCULADORA')
        self.setFixedSize(QSize(300,449))
        self.setStyleSheet('background-color: white;')
        
        self.resultado_janela=QLabel(self)
        self.resultado_janela.setGeometry(1,10,300,60)
        self.resultado_janela.setStyleSheet('border: 1px solid black;')
        self.resultado_janela.setStyleSheet('background-color: grey;')
        
        self.button_clear=QPushButton(self)
        self.button_clear.setGeometry(45,90,70,60)
        self.button_clear.setText('clear')
        self.button_clear.setStyleSheet('background-color: orange;')
        
        self.button_menos=QPushButton(self)
        self.button_menos.setGeometry(115,90,70,60)
        self.button_menos.setText('-')
        self.button_menos.setStyleSheet('background-color: grey;')
    
        
        self.button_mais=QPushButton(self)
        self.button_mais.setGeometry(185,90,70,60)
        self.button_mais.setText('+')
        self.button_mais.setStyleSheet('background-color: grey;')

        
        self.button_7=QPushButton(self)
        self.button_7.setGeometry(45,150,70,60)
        self.button_7.setText('7')
        self.button_7.setStyleSheet('background-color: grey;')
        
        self.button_8=QPushButton(self)
        self.button_8.setGeometry(115,150,70,60)
        self.button_8.setText('8')
        self.button_8.setStyleSheet('background-color: grey;')
        
        self.button_9=QPushButton(self)
        self.button_9.setGeometry(185,150,70,60)
        self.button_9.setText('9')
        self.button_9.setStyleSheet('background-color: grey;')
        
        self.button_4=QPushButton(self)
        self.button_4.setGeometry(45,210,70,60)
        self.button_4.setText('4')
        self.button_4.setStyleSheet('background-color: grey;')
        
        self.button_5=QPushButton(self)
        self.button_5.setGeometry(115,210,70,60)
        self.button_5.setText('5')
        self.button_5.setStyleSheet('background-color: grey;')
        
        
        self.button_6=QPushButton(self)
        self.button_6.setGeometry(185,210,70,60)
        self.button_6.setText('6')
        self.button_6.setStyleSheet('background-color: grey;')
        
        self.button_1=QPushButton(self)
        self.button_1.setGeometry(45,270,70,60)
        self.button_1.setText('1')
        self.button_1.setStyleSheet('background-color: grey;')
        
        self.button_2=QPushButton(self)
        self.button_2.setGeometry(115,270,70,60)
        self.button_2.setText('2')
        self.button_2.setStyleSheet('background-color: grey;')
        
        
        self.button_3=QPushButton(self)
        self.button_3.setGeometry(185,270,70,60)
        self.button_3.setText('3')
        self.button_3.setStyleSheet('background-color: grey;')
        
        self.button_zero=QPushButton(self)
        self.button_zero.setGeometry(45,330,70,60)
        self.button_zero.setText('0')
        self.button_zero.setStyleSheet('background-color: grey;')
        
        self.button_dividir=QPushButton(self)
        self.button_dividir.setGeometry(115,330,70,60)
        self.button_dividir.setText('/')
        self.button_dividir.setStyleSheet('background-color: grey;')
       
        self.button_multiplicar=QPushButton(self)
        self.button_multiplicar.setGeometry(185,330,70,60)
        self.button_multiplicar.setText('*')
        self.button_multiplicar.setStyleSheet('background-color: grey;')
        
        self.button_iqual=QPushButton(self)
        self.button_iqual.setGeometry(45,390,70,60)
        self.button_iqual.setText('=')
        self.button_iqual.setStyleSheet('background-color: orange;')
        
        self.button_ponto=QPushButton(self)
        self.button_ponto.setGeometry(115,390,70,60)
        self.button_ponto.setText('.')
        self.button_ponto.setStyleSheet('background-color: grey;')
        
        self.button_porcentagem=QPushButton(self)
        self.button_porcentagem.setGeometry(185,390,70,60)
        self.button_porcentagem.setText('%')
        self.button_porcentagem.setStyleSheet('background-color: grey;')
    
        