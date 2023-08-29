from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QApplication)
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        lista=[]
        lista_fila=[]
        lista.append(lista_fila)
        
        self.setWindowTitle('FILA')
        self.setFixedSize(500,600)
        
        self.aviso=QLabel(self)
        self.aviso.setText('Cadastrar Paciente! Atenção!! tempo de espera 15 minutos')
        self.aviso.setGeometry(3,3,400,30)
        
        self.input_nome=QLineEdit(self)
        self.input_nome.setText('Nome do Paciente = ')
        self.input_nome.setGeometry(3,50,400,30)
        nome=(self.input_nome)
        lista_fila.append(nome)
        
        self.input_tel=QLineEdit(self)
        self.input_tel.setText('Numero de telefone = ')
        self.input_tel.setGeometry(3,90,400,30)
        
        
        self.input_email=QLineEdit(self)
        self.input_email.setText('email = ')
        self.input_email.setGeometry(3,130,400,30)
        
        self.input_genero=QLineEdit(self)
        self.input_genero.setText('Genero = ')
        self.input_genero.setGeometry(3,170,400,30)
        
        self.input_genero=QLineEdit(self)
        self.input_genero.setText('Ano do nascimento = ')
        self.input_genero.setGeometry(3,210,400,30)
        
        self.aviso=QLabel(self)
        self.aviso.setText('Cliente PCD ??')
        self.aviso.setGeometry(3,250,400,30)
        
        
        self.is_pcd=QCheckBox('sim',self)
        self.no_pcd=QCheckBox('não',self)
        self.is_pcd.setGeometry(3,270,400,30)
        self.no_pcd.setGeometry(50,270,400,30)
        self.is_pcd.stateChanged.connect(self.no_pcd.deleteLater)
        self.no_pcd.stateChanged.connect(self.is_pcd.deleteLater)
        
    
        
                

    