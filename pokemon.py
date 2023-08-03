from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()