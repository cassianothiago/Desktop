from PySide6.QtCore import (QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QFormLayout,QWidget)
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ##titulo da janela##
        self.setWindowTitle('Contribuinte')
        self.setFixedSize(QSize(300,180))
        
        self.cpf_Button=QPushButton('cpf',self)
        self.cpf_Button.setIcon(QIcon('button_cpf'))
        self.cpf_Button.setGeometry(60,30,70,60)
        self.cpf_Button.clicked.connect(self.cpf)
        
        self.cnpj_Button=QPushButton('cnpj',self)
        self.cnpj_Button.setIcon(QIcon('button_cnpj'))
        self.cnpj_Button.setGeometry(160,30,70,60)
        self.cnpj_Button.clicked.connect(self.cnpj)
        
    def cpf(self):
        self.nome=QLineEdit(self)
        self.renda=QLineEdit(self)
        self.saude=QLineEdit(self)
        self.calcular_button=QPushButton('clik aqui para calcular o imposto devido')
        self.calcular_button.clicked.connect(self.calcular_cpf)
        self.pagina=QFormLayout(self)
        self.pagina.addRow('nome = ',self.nome)
        self.pagina.addRow('renda = ',self.renda)
        self.pagina.addRow('saude = ',self.saude)
        self.pagina.addRow(self.calcular_button)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFORmulario)
        self.cpf_Button.deleteLater()
        self.cnpj_Button.deleteLater()
        
        
    def calcular_cpf(self):
        renda=int(self.renda.text())
        saude=int(self.saude.text())
        
        if renda>=0 and renda<=20000 and saude==0:
            imposto=renda*(0.15)
            imposto_str=str(imposto)
            
        elif renda>=0 and renda<=20000 and saude>0:
            imposto=renda*(0.15)-saude*(0.5)
            imposto_str=str(imposto)
            
        elif renda>20000 and saude>0:
            imposto=renda*(0.25)-saude*(0.5)
            imposto_str=str(imposto)
        
        elif renda>20000 and saude==0:
            imposto=renda*(0.25)
            imposto_str=str(imposto)
        
        else:
            imposto_str=('Valores inválidos !!!')
            
        self.Qlabel_imposto=QLabel(self)
        self.Qlabel_imposto.setText(imposto_str)
        self.pagina=QFormLayout(self)
        self.pagina.addRow('imposto a pagar = R$ ',self.Qlabel_imposto)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFORmulario)
        
    def cnpj(self):
        self.nome=QLineEdit(self)
        self.renda=QLineEdit(self)
        self.qta_funcionario=QLineEdit(self)
        self.calcular_button_cnpj=QPushButton('clik aqui para calcular o imposto devido')
        self.calcular_button_cnpj.clicked.connect(self.calcular_cnpj)
        self.pagina=QFormLayout(self)
        self.pagina.addRow('nome = ',self.nome)
        self.pagina.addRow('renda = ',self.renda)
        self.pagina.addRow('numero de funcionários = ',self.qta_funcionario)
        self.pagina.addRow(self.calcular_button_cnpj)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFORmulario)
        self.cpf_Button.deleteLater()
        self.cnpj_Button.deleteLater()
        
    def calcular_cnpj(self):
        renda=int(self.renda.text())
        funcionario=int(self.qta_funcionario.text())
        
        if funcionario>=0 and funcionario<10:
            imposto=renda*(0.16)
            imposto_str=int(imposto)
        
        elif funcionario>=10:
            imposto=renda*(0.14)
            imposto_str=str(imposto)
        
        else:
            imposto_str=('Valores inválidos !!!')
            
        self.Qlabel_imposto=QLabel(self)
        self.Qlabel_imposto.setText(imposto_str)
        self.pagina=QFormLayout(self)
        self.pagina.addRow('imposto a pagar = R$ ',self.Qlabel_imposto)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(self.pagina)
        self.setCentralWidget(widgetFORmulario)

app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()