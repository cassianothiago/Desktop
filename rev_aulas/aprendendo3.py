from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
import sys

class MainWindow(QMainWindow):#criando uma classe para manipular a janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello World!!!')#título da nossa janela
        button=QPushButton('Jho soy um butão')#primeiro botão da janela
        self.setCentralWidget(button)#onde colocar o botão
        button.clicked.connect(self.imprimir)#fazendo o botão ter uma função
    def imprimir(self):
        print('Thiago aprendendo PySide6')
        
    



app=QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()