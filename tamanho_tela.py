from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Meu programa")
        self.setFixedSize(QSize(600,400))
        self.lbl=QLabel("Hello Word!")
        font=self.lbl.font()
        font.setPointSize
        



app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()