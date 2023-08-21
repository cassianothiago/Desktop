import shutil
import sys
import os
from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget,QFileDialog)
from organizar import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Organizar arquivos')
        appicon=QIcon('pasta3.png')
        self.setWindowIcon(appicon)
        
    def open_path(self):
        self.path=QFileDialog.getExistingDirectory(self,str('pasta com arquivos'),'\home',QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.qline.setText(self.path)
        self.path=str(self.path)


app=QApplication(sys.argv)
w=QMainWindow
ui=Ui_MainWindow
ui.setupUi(w)
w.show
app.exec