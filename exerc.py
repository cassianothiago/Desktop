import sys
from typing import Optional
import PySide6.QtCore 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout, QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('janela principal')
        self.setFixedSize(800,400)
        
        self.button=QPushButton('Abrir janela secundária',self)
        self.button.clicked.connect(self.open_secundary_window)
        self.button.setGeometry(100,100,500,100)
        
    def open_secundary_window(self):
        self.secundary_Window=SecundaryWindow()
        self.secundary_Window.show()
        
class SecundaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('janela secundária')
        self.setGeometry(200,200,500,300)
        layout=QVBoxLayout()
        label=QLabel('picaxu do xoque')
        layout.addWidget(label)
        imagem_label=QLabel(self)
        pixmap=QPixmap("picachu.jpg") 
        imagem_label.setPixmap(pixmap)
        layout.addWidget(imagem_label)

        close_button = QPushButton("Fechar", self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()