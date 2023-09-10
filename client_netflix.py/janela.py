from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget)
import sys
from cliente import*
from botão import*


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Cadastro de Cliente')
        self.setFixedSize(QSize(700,500))
        
        self.input_nome_cliente=QLineEdit(self)
        self.input_nome_cliente.setText('nome: ')
        self.input_nome_cliente.setGeometry(10,30,320,30)
        nome=self.input_nome_cliente
        self.button_nome=QPushButton(self)
        self.button_nome.setText('confirma!')
        self.button_nome.setGeometry(330,30,80,30)
        clicarnome=Button()
        self.button_nome.clicked.connect(clicarnome.clicar_nome(nome))
        
        self.input_email_cliente=QLineEdit(self)
        self.input_email_cliente.setText('email: ')
        self.input_email_cliente.setGeometry(10,60,320,30)
        email=self.input_email_cliente
        