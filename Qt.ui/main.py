from typing import Optional
import tela_loguin_senha2_ui

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import icons2
import sys

class MainWindown(QMainWindow,tela_loguin_senha2_ui):
    def  __init__(self):
        super().__init__()
        
if __name__=='__main__':
    app=QApplication
    w=MainWindown
    w.show()
    app.exec()
    