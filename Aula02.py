
import PySide6.QtCore
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QLabel
from PySide6.QtCore import QSize,Qt
import sys

class MainWindown(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu programa qlabel')#define o titulo da janela 
        self.setFixedSize(QSize(600,400))#define o tamanho fixo da janela
        
        #crinado um rotulo qlabel com texto e configuração de alinhamento
        self.lbl=QLabel('hello world')
        font=self.lbl.font()
        font.setPointSize(35)
        self.lbl=QLabel('helo world',self)
        
        frontTitulo=self.lbl.font