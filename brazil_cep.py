from typing import Optional
import PySide6.QtCore
import brazilcep
import sys
from PySide6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('buscar cep')

dig=input('digitar= ')        
enderero=brazilcep.get_address_from_cep(dig)
print(enderero)

app=QApplication(sys.argv)
window=MainWindow
window.show()
app.exec()