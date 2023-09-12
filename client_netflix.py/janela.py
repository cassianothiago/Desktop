from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QWidget,)
from PySide6.QtGui import QPixmap
from cliente import*



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Cadastro de Cliente')
        self.setFixedSize(QSize(700,500))
        
        self.welcome_cliente=QLabel(self)
        self.welcome_cliente.setText('Bem vindo ao cadastro de cliente')
        self.welcome_cliente.setGeometry(10,1,320,20)
        
        self.input_nome_cliente=QLineEdit(self)
        self.input_nome_cliente.setText('Nome: ')
        self.input_nome_cliente.setGeometry(10,30,320,30)
        self.nome=self.input_nome_cliente
        
        
        self.input_email_cliente=QLineEdit(self)
        self.input_email_cliente.setText('Email: ')
        self.input_email_cliente.setGeometry(10,60,320,30)
        self.email=self.input_email_cliente
        
        self.input_cpf_cliente=QLineEdit(self)
        self.input_cpf_cliente.setText('CPF: ')
        self.input_cpf_cliente.setGeometry(10,90,320,30)
        self.cpf=self.input_cpf_cliente
        
        self.input_senha_cliente=QLineEdit(self)
        self.input_senha_cliente.setText('Senha: ')
        self.input_senha_cliente.setGeometry(10,120,320,30)
        self.senha=self.input_cpf_cliente
        
        self.button_cadastrar=QPushButton(self)
        self.button_cadastrar.setText('CADASTRAR !!')
        self.button_cadastrar.setGeometry(10,150,320,30)
        self.button_cadastrar.clicked.connect(self.cadastrar)
        
        
        self.imagem_cadastro=QLabel(self)
        self.imagem_cadastro.setPixmap(QPixmap('imagem_cadastro.png'))
        self.imagem_cadastro.setGeometry(350,30,320,150)
        
    def cadastrar(self):
        cliente=Cliente('a','b','c','d','basic')
        self.mostrar_cadastro=QLabel(self)
        self.mostrar_cadastro.setText(cliente.nome)
        self.mostrar_cadastro.setGeometry((10,150,320,300))
       
    
            
