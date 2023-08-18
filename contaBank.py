
from PySide6.QtWidgets import (QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider,QLayout)

from PySide6.QtCore import (Qt,QSize)

from PySide6.QtGui import (QPalette,QColor)

import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,QVBoxLayout,QHBoxLayout)

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ##titulo da janela##
        self.setWindowTitle('Seu Banco')
        self.setFixedSize(QSize(700,500))
        
        ##linhas para digitar a agencia e conta##
        self.agencia=QLineEdit(self)
        self.conta=QLineEdit(self)
        
        ##label para perguntar se deseja deposito inicial##
        self.pergunta=QLabel('Deseja fazer deposito inicial?')
    
        ##chekbox para responder a pergunta do deposito inicial##
        self.depositoS=QCheckBox('sim')
        self.depositoN=QCheckBox('não')
        self.depositoS.stateChanged.connect(self.state)
        self.depositoN.stateChanged.connect(self.state2)
        
        ##linha para digitar o valor do dep inicial##
        self.valorDepInicial_Qline=QLineEdit(self)
        
        ##label para mostrar o valor digitado 
        self.valorDepInicial_Qlabel=QLabel(self.valorDepInicial_Qline)
        
        #botão para abrir a conta#
        self.abrirContaButton=QPushButton('Abrir conta',self)
        self.abrirContaButton.clicked.connect(self.cadastrar_conta)
        
        #espaço que mostra os dados da conta
        self.registrarConta=QLabel(self)
        
        ##formatação dos Widgets##
        pagina=QFormLayout(self)
        pagina.addRow('Agência = ',self.agencia)
        pagina.addRow('Conta = ',self.conta)
        pagina.addRow(self.pergunta)
        pagina.addRow(self.depositoS)
        pagina.addRow(self.depositoN)
        pagina.addRow('valor que deseja depositar = ',self.valorDepInicial_Qline)
        pagina.addRow('total dep = ',self.valorDepInicial_Qlabel)
        pagina.addRow(self.abrirContaButton)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(pagina)
        self.setCentralWidget(widgetFORmulario)
        
        
    def state(self,s):#se tiver dep inicial#
        if s == 2:
            self.depositoN.deleteLater() 
            valor=(self.valorDepInicial_Qline.text())
            self.valorDepInicial_Qlabel=valor
        
    def state2(self, s):#se não tiver dep inicial#
        if s == 2:
            self.depositoS.deleteLater()
            valor=(self.valorDepInicial_Qlabel.text('0'))
            self.valorDepInicial_Qlabel=valor
        
    def cadastrar_conta(self):
        pagina=QFormLayout
        self.depositoN.deleteLater()
        pagina.addRow('Abertura realizada com sucesso!!',self.registrarConta)  
        self.registrarConta('Agência = {}\nConta = {}\nValor = {}'
        .format(self.agencia.text(), self.conta.text(), self.valorDepInicial_Qlabel.text()))
        
app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()
sys.exit(app.exec_())