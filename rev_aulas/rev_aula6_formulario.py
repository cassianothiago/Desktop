from typing import Optional
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette,QColor
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,QVBoxLayout,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('formulario')
        
        self.dgit_numero1=QLineEdit(self)
        self.dgit_numero2=QLineEdit(self)
        
        self.botao=QPushButton('somar',self)
        self.botao.clicked.connect(self.calcular)
        
        self.resposta=QLabel(self)
        
        pagina=QFormLayout(self)
        pagina.addRow('primeiro número = ',self.dgit_numero1)
        pagina.addRow('segundo número = ',self.dgit_numero2)
        pagina.addRow(self.botao)
        pagina.addRow(self.resposta)
        widget = QWidget()
        widget.setLayout(pagina)

        self.setCentralWidget(widget)
                

    def calcular(self):
        numero1=int(self.dgit_numero1.text())
        numero2=int(self.dgit_numero2.text())
        soma=numero1+numero2
        self.resposta.setText('resposta = {}'.format(soma))
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()