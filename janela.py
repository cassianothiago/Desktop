from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vai ficar pior')
        self.setFixedSize(QSize(600,400))
        self.lbl=QLabel
        font=self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)
app=QApplication(sys.argv) #lista de argumento'''
janela=MainWindow()#janela
janela.show()
app.exec()
