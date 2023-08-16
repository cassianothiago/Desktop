from typing import Optional
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import (Qt)
from PySide6.QtGui import (QPalette,QColor)
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
    QVBoxLayout,QHBoxLayout)

import brazilcep

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Pesquisa CEP')
        
        self.dgit_cep=QLineEdit(self)
        
        self.button=QPushButton('pesquisar',self)
        self.button.clicked.connect(self.pesq_cep)
        
        self.resposta=QLabel(self)
        
        pagina=QFormLayout(self)
        pagina.addRow(self.dgit_cep)
        pagina.addRow(self.button)
        pagina.addRow(self.resposta)
        widget = QWidget(self)
        widget.setLayout(pagina)
        self.setCentralWidget(widget)
        
    def pesq_cep(self):
        cep_text=self.dgit_cep(cep)
        cep=brazilcep.get_address_from_cep(cep_text)
        self.resposta=cep


app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()

