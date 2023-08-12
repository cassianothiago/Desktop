from PySide6.QtWidgets import QApplication,QWidget
import sys

#inicialização a aplicação
app=QApplication(sys.argv)

#criando uma instacia da janela Qwidget para representar uma janela 
janela=QWidget()

#exibindo a janela para usuario 
janela.show()

#iniciando loop de evento da aplicação
app.exec()