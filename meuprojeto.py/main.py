'''import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDialog, QFormLayout, QMessageBox


from exibirRelatorio import ExibirRelatorio
from folhaPagamento import FolhaDePagamento
from formularioFuncionarioTerceirizado import FormularioFuncionarioTerceirizado
from funcionario import Funcionario
from funcionarioTerceirizado import FuncionarioTerceirizado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Funcionario()
    window.show()
    sys.exit(app.exec_())'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDialog, QFormLayout, QMessageBox

from modulo.funcionario import Funcionario

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Funcionario()
    window.show()
    sys.exit(app.exec_())