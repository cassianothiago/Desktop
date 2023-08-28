from janela import*
import sys
from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLabel, QLineEdit,
QCheckBox,QFormLayout,QWidget,QApplication)


app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec()