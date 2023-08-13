
from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QLabel
from PySide6.QtCore import QSize,Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Minha janela')
        self.setFixedSize(QSize(600,400))
        
        self.label=QLabel('Minha Qlabel')
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.label)

app=QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()
