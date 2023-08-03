import typing
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
import sys

'''class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hello World!!!")
		button = QPushButton("Jho soy um butão")
		self.setCentralWidget(button)
		button.clicked.connect(self.imprimir)
	def imprimir(self):
		print("Professor Maurício")'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.setWindowTitle('Meu Programa')
        self.setFixedSize(600,400)
        
        
  
  
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec_()