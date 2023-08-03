from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokedex")
        self.setGeometry(100,100,300,150)
        
        self.label1 = QLabel("Pokemom 1", self)
        self.label1.setGeometry(10,10,80,30)
        
        self.label2 = QLabel("Pokemo 2", self)
        self.label2.setGeometry(10,50,80,30)
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        
        
        
    def calcular(self):
        pokemon1 = (self.input1.text())
        pokemon2 = (self.input2.text())
        self.result_label.setText(f"O resultado da soma é {soma}")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()