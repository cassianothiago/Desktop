from PySide6.QtCore import (QSize)
from PySide6.QtGui import (QIcon,QPixmap)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QToolButton)
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ##titulo da janela##
        self.setWindowTitle('Contribuinte')
        self.setFixedSize(QSize(700,500))
        
        self.cpf_Button=QPushButton('cpf',self)
        self.cpf_Button.setIcon(QIcon('button_cpf'))
        self.cpf_Button.setGeometry(60,30,70,60)
        
        self.cnpj_Button=QPushButton('cnpj',self)
        self.cnpj_Button.setIcon(QIcon('button_cnpj'))
        self.cnpj_Button.setGeometry(160,30,70,60)
        
    def cpf(self):
        self.nome=QLineEdit(self)
        self.renda=QLineEdit(self)
        self.saude=QLineEdit(self)
        self.calcular=QPushButton(self)
    def calcular_cpf(self):
        renda=int(self.renda)
        imposto=renda*(0.15)
        self.Qlabel_imposto=QLabel(self)
        self.Qlabel_imposto.text
        
    

app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()