import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDialog, QFormLayout, QMessageBox

class ExibirRelatorio(QDialog):
 def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Funcionário Terceirizado")
        self.setGeometry(200, 200, 400, 300)

        self.layout = QFormLayout()

        for elemento in lista_funcionarios:
            nova_lista_KKK.append(str(elemento))
        # Exemplo de lista
        minha_lista = ["Item 1", "Item 2", "Item 3", "Item 4"]

        # Converter a lista em uma única string 
        lista_como_string = "\n".join(nova_lista_KKK)

        # Cria Label para exibir a lista
        self.label = QLabel(lista_como_string)
        self.layout.addRow(self.label)


        self.setLayout(self.layout)
