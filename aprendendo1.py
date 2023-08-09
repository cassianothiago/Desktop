from PySide6.QtWidgets import QApplication, QWidget
import sys
#qtwingets cria e gerencia recursos de elementos gráficos
#QApplication é a aplicação em si para iniciar a execução gráfica
#import sys biblioteca padrão python parecido com os

app=QApplication(sys.argv)
#usando o parametro sys.arg vc permite que o PySide6 acesso os argumentos do sys
janela=QWidget()
#criando a janela 
janela.show()
#exibe a janela
app.exec
#método para o loop de execução para responder as interações