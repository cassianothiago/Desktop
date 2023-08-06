from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio nº 5")
        self.setGeometry(100,100,300,150)
        
        self.label1 = QLabel("Valor em\nMetros", self)
        self.label1.setGeometry(5,10,80,30)
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(80,10,80,30)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(180,90,280,30)
        
        self.button = QPushButton("Converter cm", self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.calcular)
        
    def calcular(self):
        num1 = int(self.input1.text())
        cent = num1*100
        self.result_label.setText(f"O valor em centímetros é =  {cent} cm")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()