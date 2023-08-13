from typing import Optional
from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton,QHBoxLayout
from PySide6.QtCore import QSize,Qt
from PySide6.QtGui import QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QBox')
        
        self.widget=QWidget()
        self.setCentralWidget(self.widget)
        
        self.lugar=QHBoxLayout()
        self.widget.setLayout(self.lugar)
        
        self.botao1=QPushButton('botao 1')
        self.clicar=print('clicado')
        self.botao1.clicked.connect(self.clicar)
        self.lugar.addWidget(self.botao1)
            
    

app=QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec()