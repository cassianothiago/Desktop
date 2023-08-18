from PySide6.QtWidgets import QApplication, QMainWindow, QFormLayout, QWidget, QLabel, QCheckBox, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QSize
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Seu Banco')
        self.setFixedSize(QSize(700, 500))
        
        self.agencia = QLineEdit(self)
        self.conta = QLineEdit(self)
        
        self.pergunta = QLabel('Deseja fazer depósito inicial?')
        self.depositoS = QCheckBox('Sim')
        self.depositoN = QCheckBox('Não')
        self.depositoS.stateChanged.connect(self.state)
        self.depositoN.stateChanged.connect(self.state2)
        
        self.valorDepInicial = QLineEdit(self)
        
        self.depositoInicial = QLabel(self)
        
        self.depositar = QPushButton('Abrir conta', self)
        self.depositar.clicked.connect(self.cadastrar_conta)
        
        self.abrir_conta = QLabel(self)
        
        pagina = QFormLayout(self)
        pagina.addRow('Agência = ', self.agencia)
        pagina.addRow('Conta = ', self.conta)
        pagina.addRow(self.pergunta)
        pagina.addRow(self.depositoS)
        pagina.addRow(self.depositoN)
        pagina.addRow('Valor = ', self.valorDepInicial)
        pagina.addRow('Total dep = ', self.depositoInicial)
        pagina.addRow(self.depositar)
        pagina.addRow(self.abrir_conta)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(pagina)
        self.setCentralWidget(widgetFORmulario)
        
    def state(self, s):
        if s == Qt.Checked:
            self.depositoN.deleteLater() 
            valor = self.valorDepInicial.text()
            self.depositoInicial.setText(valor)
        
    def state2(self, s):
        if s == Qt.Checked:
            self.depositoS.deleteLater()
            self.valorDepInicial.setText('0')
            self.depositoInicial.setText('0')
        
    def cadastrar_conta(self):
        self.abrir_conta.setText('Agência = {}\nConta = {}\nValor = {}'
        .format(self.agencia.text(), self.conta.text(), self.depositoInicial.text()))
        
app = QApplication(sys.argv)
w = Mainwindow()
w.show()
sys.exit(app.exec_())