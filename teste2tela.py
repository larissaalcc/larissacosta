import sys
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import Qdialog
class Tela2(QDialog):
    
    def __init__(self, parent = None):
        #chamando o contrutor de Qdialog
        super(Tela2, self).__init__(parent)

class TelaLogin(QWidget):

    def __init__(self):
        super(TelaLogin, self).__init__(None)
        
        #criando os botoes
        Cadastrar = QPushButton('Cadastrar', self)
        
        # abrindo a seguunda tela quando clicar no botao cadastrar - isso atraves do click do botao
        Cadastrar.clicked.connect(self.AbreTela2)
        
    def AbreTela2(self):
        t = Tela2(self)
        t.show()
        t.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app = TelaLogin()
    app.show()
    app.exec_()