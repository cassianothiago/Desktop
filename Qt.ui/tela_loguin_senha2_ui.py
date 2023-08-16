# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_loguin_senha2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import icons2
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(588, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameprincipal = QFrame(self.centralwidget)
        self.frameprincipal.setObjectName(u"frameprincipal")
        self.frameprincipal.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.frameprincipal.setFrameShape(QFrame.StyledPanel)
        self.frameprincipal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameprincipal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frameusuario = QFrame(self.frameprincipal)
        self.frameusuario.setObjectName(u"frameusuario")
        self.frameusuario.setFrameShape(QFrame.StyledPanel)
        self.frameusuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameusuario)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.imagem = QLabel(self.frameusuario)
        self.imagem.setObjectName(u"imagem")
        self.imagem.setPixmap(QPixmap(u":/icon/transferir.jpeg"))
        self.imagem.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.imagem)

        self.usuario = QLabel(self.frameusuario)
        self.usuario.setObjectName(u"usuario")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.usuario.setFont(font)

        self.verticalLayout_3.addWidget(self.usuario)

        self.digusuario = QLineEdit(self.frameusuario)
        self.digusuario.setObjectName(u"digusuario")

        self.verticalLayout_3.addWidget(self.digusuario)


        self.verticalLayout_4.addWidget(self.frameusuario)

        self.framesenha = QFrame(self.frameprincipal)
        self.framesenha.setObjectName(u"framesenha")
        self.framesenha.setFrameShape(QFrame.StyledPanel)
        self.framesenha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.framesenha)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.senha = QLabel(self.framesenha)
        self.senha.setObjectName(u"senha")
        self.senha.setFont(font)

        self.verticalLayout_2.addWidget(self.senha)

        self.digsenha = QLineEdit(self.framesenha)
        self.digsenha.setObjectName(u"digsenha")
        self.digsenha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.digsenha)


        self.verticalLayout_4.addWidget(self.framesenha)


        self.verticalLayout.addWidget(self.frameprincipal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imagem.setText("")
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"usuario", None))
        self.digusuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digitar_usuario", None))
        self.senha.setText(QCoreApplication.translate("MainWindow", u"senha", None))
        self.digsenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digitar_senha", None))
    # retranslateUi

app=QApplication(sys.argv)
w = QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(w)
w.show()
app.exec()