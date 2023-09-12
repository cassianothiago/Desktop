from PySide6.QtWidgets import QApplication
import sys
from janela import*


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()