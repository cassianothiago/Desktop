from typing import Optional
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import (Qt,QSize)
from PySide6.QtGui import (QPalette,QColor)
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
    QVBoxLayout,QHBoxLayout)

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Seu Banco')
        self.setFixedSize(QSize(400,200))
        
        self.agencia=QLineEdit(self)
        self.conta=QLineEdit(self)
        
        self.pergunta=QLabel('Deseja fazer deposito inicial?')
        
        
        self.depositoS=QCheckBox('sim')
        self.depositoN=QCheckBox('não')
        self.depositoS.stateChanged.connect(self.state)
        self.depositoN.stateChanged.connect(self.state2)
        

        self.valorDepInicial=QLineEdit(self)
        
        self.depositoInicial=QLabel(self)
        
        self.depositar=QPushButton('Abrir conta',self)
        
        pagina=QFormLayout(self)
        pagina.addRow('Agência = ',self.agencia)
        pagina.addRow('Conta = ',self.conta)
        pagina.addRow(self.pergunta)
        pagina.addRow(self.depositoS)
        pagina.addRow(self.depositoN)
        pagina.addRow('valor = ',self.valorDepInicial)
        pagina.addRow('total dep = ',self.depositoInicial)
        pagina.addRow(self.depositar)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(pagina)
        self.setCentralWidget(widgetFORmulario)
        
        
    def state(self,s):
        if s == 2:
            self.depositoN.deleteLater() 
            valor=(self.valorDepInicial.text())
            self.depositoInicial.setText(valor)
            return valor
    def state2(self, s):
        if s == 2:
            self.depositoS.deleteLater()
            valor=(self.valorDepInicial.setText('0'))
            self.depositoInicial.setText(valor)
            return valor
        
        
        
app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()