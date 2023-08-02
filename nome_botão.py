from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow 
import sys

class MainWindow(QMainWindow):
	def _init_(self):
		super()._init_()
		self.setWindowTitle("Hello World!!!")
		button = QPushButton("Jho soy um butão")
		self.setCentralWidget(button)
		button.clicked.connect(self.imprimir)
	def imprimir(self):
		print("Thiago")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()