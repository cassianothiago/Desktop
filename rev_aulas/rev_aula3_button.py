from typing import Optional
from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton
from PySide6.QtCore import QSize,Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('minha janela')
        botao=QPushButton('click')
        self.setCentralWidget(botao)
        botao.clicked.connect(self.imprimir)
        
    def imprimir(self):
        print('clicou')
        
        
        
app=QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()