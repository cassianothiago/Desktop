
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
        
        self.setWindowTitle('Seu Banco')
        self.setFixedSize(QSize(700,500))
        
        self.agencia=QLineEdit(self)
        self.agenciaText = self.agencia.text()
        self.conta=QLineEdit(self)
        
        self.pergunta=QLabel('Deseja fazer deposito inicial?')
    
        
        self.depositoS=QCheckBox('sim')
        self.depositoN=QCheckBox('não')
        self.depositoS.stateChanged.connect(self.state)
        self.depositoN.stateChanged.connect(self.state2)
        

        self.valorDepInicial_Qline=QLineEdit(self)
        
        self.valorDepInicial_Qlabel=QLabel(self)
        
        self.depositar=QPushButton('Abrir conta',self)
        self.depositar.clicked.connect(self.cadastrar_conta)
        
        self.abrir_conta=QLabel(self)
        
        pagina=QFormLayout(self)
        pagina.addRow('Agência = ',self.agencia)
        pagina.addRow('Conta = ',self.conta)
        pagina.addRow(self.pergunta)
        pagina.addRow(self.depositoS)
        pagina.addRow(self.depositoN)
        pagina.addRow('valor = ',self.valorDepInicial_Qline)
        pagina.addRow('total dep = ',self.valorDepInicial_Qlabel)
        pagina.addRow(self.depositar)
        pagina.addRow(self.abrir_conta)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(pagina)
        self.setCentralWidget(widgetFORmulario)
        
        
    def state(self,s):
        if s == 2:
            self.depositoN.deleteLater() 
            valor=(self.valorDepInicial_Qline())
            self.valor(valor)
            return valor
        
    def state2(self, s):
        if s == 2:
            self.depositoS.deleteLater()
            valor=(self.valorDepInicial_Qline.text('0'))
            return valor
        
    def cadastrar_conta(self):
        self.depositoN.deleteLater()  
        self.abrir_conta.setText('Agência = {}\nConta = {}\nValor = {}'
        .format(self.agencia.text(), self.conta.text(), self.valorDepInicial_Qline.text()))
        
app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()
sys.exit(app.exec_())