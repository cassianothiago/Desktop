import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exercio entreque n 2')
        self.button=QPushButton('somar',self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.imprimir)
        self.resultado=QLabel(self)
        self.resultado.setGeometry(10,220,280,30)
        self.digitar1=QLineEdit(self)
        self.digitar1.setGeometry(100,10,80,30)
        self.digitar2=QLineEdit(self)
        self.digitar2.setGeometry(100,50,80,30)
        
    def imprimir(self):
        numero1=int(self.digitar1.text())
        numero2=int(self.digitar2.text())
        soma=numero1+numero2
        print(soma)
        
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()