
from PySide6.QtCore import (QSize)
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget)

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lista=[]#saldo da conta
        
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
        self.totaldep=self.valorDepInicial_Qline.text()
        
        ##label para mostrar o valor digitado 
        self.valorDepInicial_Qlabel=QLabel()
        
        
        #botão para abrir a conta#
        self.abrirContaButton=QPushButton('Abrir conta',self)
        self.abrirContaButton.clicked.connect(self.cadastrar_conta)
        
        #espaço que mostra os dados da conta
        self.registrarConta=QLabel(self)
        
        #botao para depositar
        self.depButton=QPushButton('Depositar',self)
        self.depButton.clicked.connect(self.depositar)
        
        #linha para digitar o valor dep apos abertura da conta
        self.valor_Qline=QLineEdit(self)
        
        #label para mostrar o resultado do dep apos abertura da conta
        self.valor_Qlabel=QLabel(self)
        
        #botao sacar
        self.sacar_QButon=QPushButton('Sacar',self)
        self.sacar_QButon.clicked.connect(self.sacar)
        
        #linha para sacar
        self.sacar_Qline=QLineEdit(self)
        
        #label para mostrar o resultado do saque
        self.sacar_Qlabel=QLabel()
        
        ##formatação dos Widgets##
        pagina=QFormLayout(self)
        pagina.addRow('Agência = ',self.agencia)
        pagina.addRow('Conta = ',self.conta)
        pagina.addRow(self.pergunta)
        pagina.addRow(self.depositoS)
        pagina.addRow(self.depositoN)
        pagina.addRow('valor que deseja depositar = ',self.valorDepInicial_Qline)
        pagina.addRow(self.abrirContaButton)
        pagina.addRow(self.registrarConta)
        pagina.addRow('Valor do deposito = ',self.valor_Qline)
        pagina.addRow(self.depButton)
        pagina.addRow(self.valor_Qlabel)
        pagina.addRow('valor do saque(ATENÇÃO!! cobrança de R$ 5,00 por saque) = ',self.sacar_Qline)
        pagina.addRow(self.sacar_QButon)
        pagina.addRow(self.sacar_Qlabel)
        widgetFORmulario = QWidget()
        widgetFORmulario.setLayout(pagina)
        self.setCentralWidget(widgetFORmulario)
        
        
    def state(self,s):#se tiver dep inicial#
        if s == 2:
            self.depositoN.deleteLater() 
            valor=self.valorDepInicial_Qline.text()
            dep=int(valor)
            self.lista.append(dep)
            self.valorDepInicial_Qlabel=valor
            
            
    def state2(self, s):#se não tiver dep inicial#
        if s == 2:
            self.depositoS.deleteLater()
            self.valorDepInicial_Qline.setText('0')
            self.valorDepInicial_Qlabel.setText('R$ 0,00')
            self.lista.append(0)
            
    def cadastrar_conta(self):
        self.registrarConta.setText('Conta Aberta com sucesso!!!\nAgência = {}\nConta = {}\nSaldo = R$ {},00'
        .format(self.agencia.text(), self.conta.text(), self.valorDepInicial_Qline.text()))

    def depositar(self):
        inicial=self.valorDepInicial_Qline.text()
        posterior=self.valor_Qline.text()
        dep=int(inicial)+int(posterior)
        self.valor_Qlabel.setText('Saldo = R$ {},00'.format(dep))
        self.lista.append(dep)
        
    def sacar(self):
        sacar=self.sacar_Qline.text()
        saldo=(sum(self.lista)-int(sacar))-5
        if saldo>=0:
            self.sacar_Qlabel.setText('saldo  = R$ {},00'.format(saldo))
        else:
            self.sacar_Qlabel.setText('Saldo insuficiente!!\nFavor entrar em contato com seu gerente para uma possível liberação de limite de conta')
        
app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()