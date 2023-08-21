# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizar.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import organizartexto_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(585, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.qlabel = QLabel(self.frame_2)
        self.qlabel.setObjectName(u"qlabel")
        self.qlabel.setMinimumSize(QSize(521, 0))
        self.qlabel.setPixmap(QPixmap(u":/organizar/pasta3.png"))
        self.qlabel.setScaledContents(True)

        self.gridLayout.addWidget(self.qlabel, 1, 0, 1, 2)

        self.ok = QPushButton(self.frame_2)
        self.ok.setObjectName(u"ok")
        self.ok.setEnabled(True)
        self.ok.setMinimumSize(QSize(150, 30))
        self.ok.setCursor(QCursor(Qt.OpenHandCursor))
        self.ok.setStyleSheet(u"QPushButton{\n"
"	rgb(255, 255, 255)\n"
"	background-color: rgb(0, 0, 0);\n"
"border-top-right-radius:15px;\n"
"}")

        self.gridLayout.addWidget(self.ok, 2, 1, 1, 1)

        self.qline = QLineEdit(self.frame_2)
        self.qline.setObjectName(u"qline")
        self.qline.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.qline, 2, 0, 1, 1)

        self.organizar = QPushButton(self.frame_2)
        self.organizar.setObjectName(u"organizar")

        self.gridLayout.addWidget(self.organizar, 3, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.qlabel.setText("")
        self.ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.qline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"selecione uma pasta", None))
        self.organizar.setText(QCoreApplication.translate("MainWindow", u"organizar", None))
    # retranslateUi

