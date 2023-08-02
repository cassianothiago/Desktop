from typing import Optional
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PySide6.QtCore import QSize
import sys
 
class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Exercício 2")
        self.button= QPushButton("Botão", self)
        self.button.setGeometry(190,10,100,70)
        self.result_label= QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        self.button.clicked.connect(self.Imprimir)
        
    def Imprimir(self):
        numero=5
        if numero % 2==0:
            self.result_label.setText(f"O número informado foi o número {numero}, e é par")
        else:
            self.result_label.setText(f"O número informado foi o número {numero}, e é ímpar")

app= QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()