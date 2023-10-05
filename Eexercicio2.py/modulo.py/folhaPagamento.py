import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDialog, QFormLayout, QMessageBox

class FolhaDePagamento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folha de Pagamento")
        self.setGeometry(100, 100, 300, 100)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()



        self.label = QLabel("[1] - Regular [2] - Terceirizado\nInsira o tipo de Funcionário:")
        self.layout.addWidget(self.label)

        self.input_funcionario = QLineEdit()
        self.layout.addWidget(self.input_funcionario)

        self.button = QPushButton("Adicionar Funcionário")
        self.button.clicked.connect(self.abrirFormulario)
        self.layout.addWidget(self.button)

        self.button_relatorio = QPushButton("Imprimir Relatorio")
        self.button_relatorio.clicked.connect(self.relatorio)
        self.layout.addWidget(self.button_relatorio)

        # Converter a lista em uma única string separada por quebras de linha
        lista_como_string = "\n".join(lista_funcionarios)

        # Cria label pra mostrar a lista
        self.label = QLabel(lista_como_string)
        self.layout.addWidget(self.label)

        self.central_widget.setLayout(self.layout)

        self.funcionarios = []  # Lista para armazenar funcionários
    
    def relatorio(self):
        relatorio = ExibirRelatorio()
        if relatorio.exec_():
            funcionario = relatorio.funcionario
            self.funcionarios.append(funcionario)
            self.atualizarTextEdit()

    def abrirFormulario(self):
        escolha = int(self.input_funcionario.text())
        if (escolha == 1):
            formulario = FormularioFuncionarioRegular()
            if formulario.exec_():
                funcionario = formulario.funcionario
                self.funcionarios.append(funcionario)
                self.atualizarTextEdit()
        elif (escolha == 2):
            formulario = FormularioFuncionarioTerceirizado()
            if formulario.exec_():
                funcionario = formulario.funcionario
                self.funcionarios.append(funcionario)
                self.atualizarTextEdit()


    def atualizarTextEdit(self):
        self.text_edit.clear()
        for func in self.funcionarios:
            if isinstance(func, FuncionarioTerceirizado):
                pagamento = func.valor_hora * func.horas_trabalhadas + 1.1 * func.despesa_adicional
                self.text_edit.append(f"Nome: {func.nome}, Pagamento: R${pagamento:.2f}")
            else:
                pagamento = func.valor_hora * func.horas_trabalhadas
                self.text_edit.append(f"Nome: {func.nome}, Pagamento: R${pagamento:.2f}")

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
