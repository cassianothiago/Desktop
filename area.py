import sys
from shape import*
from retangulo import*
from circulo import*
import PySide6.QtCore 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('calculo de área')
        self.setFixedSize(800,400)
        
        self.button=QPushButton('Retangulo',self)
        self.button.clicked.connect(self.)
        self.button.setGeometry(10,10,80,30)
        self.button2=QPushButton('Circulo',self)
        self.button2.clicked.connect(self.open_secundary_window)
        self.button2.setGeometry(10,50,80,30)
        
        
    def open_secundary_window(self):
        self.secundary_Window=Rentagulo()
        self.secundary_Window.show()
        
class Rentagulo(QDialog):
    def __init__(self):
        super().__init__()
        self.button=QPushButton('calcular',self)
        self.cal=QLineEdit()
        base=float(self.cal.text())
        altura=float(self.cal.text())
        
        calculo=Rentagulo
        self.button.clicked.connect(base,altura)
        self.setWindowTitle('janela secundária')
        self.setGeometry(200,200,500,300)
        layout=QVBoxLayout()
        label=QLabel('retangulo')
        layout.addWidget(label)
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        close_button = QPushButton("Fechar", self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()