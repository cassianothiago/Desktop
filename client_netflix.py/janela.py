from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, 
QLineEdit)
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
        
        self.rotulo_nome=QLabel(self)
        self.rotulo_nome.setText('Nome ')
        self.rotulo_nome.setGeometry(1,30,50,30)
        self.input_nome_cliente=QLineEdit(self)
        self.input_nome_cliente.setGeometry(60,30,320,30)
        self.nome=self.input_nome_cliente
        
        self.rotulo_email=QLabel(self)
        self.rotulo_email.setText('Email ')
        self.rotulo_email.setGeometry(1,60,50,30)
        self.input_email_cliente=QLineEdit(self)
        self.input_email_cliente.setGeometry(60,60,320,30)
        self.email=self.input_email_cliente
        
        self.rotulo_cpf=QLabel(self)
        self.rotulo_cpf.setText('CPF ')
        self.rotulo_cpf.setGeometry(1,90,50,30)
        self.input_cpf_cliente=QLineEdit(self)
        self.input_cpf_cliente.setGeometry(60,90,320,30)
        self.cpf=self.input_cpf_cliente
        
        self.rotulo_senha=QLabel(self)
        self.rotulo_senha.setText('Senha ')
        self.rotulo_senha.setGeometry(1,120,50,30)
        self.input_senha_cliente=QLineEdit(self)
        self.input_senha_cliente.setGeometry(60,120,320,30)
        self.senha=self.input_cpf_cliente
        
        self.rotulo_button=QLabel(self)
        self.rotulo_button.setText('-->')
        self.rotulo_button.setGeometry(8,150,50,30)
        self.button_cadastrar=QPushButton(self)
        self.button_cadastrar.setText('CADASTRAR !!')
        self.button_cadastrar.setGeometry(60,150,320,30)
        #self.button_cadastrar.clicked.connect(self.cadastrar)
        
        self.imagem_cadastro=QLabel(self)
        self.imagem_cadastro.setPixmap(QPixmap('imagem_cadastro.png'))
        self.imagem_cadastro.setGeometry(420,30,320,150)
        
    '''def cadastrar(self):
        cliente=Cliente('a','b','c','d','basic')
        self.mostrar_cadastro=QLabel(self)
        self.mostrar_cadastro.setText(cliente.nome)
        self.mostrar_cadastro.setGeometry((10,150,320,300))'''
       
    
            
