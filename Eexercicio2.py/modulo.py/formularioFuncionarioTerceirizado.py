import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDialog, QFormLayout, QMessageBox

class FormularioFuncionarioTerceirizado(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Funcionário Terceirizado")
        self.setGeometry(200, 200, 400, 300)

        layout = QFormLayout()

        self.nome_label = QLabel("Nome:")
        self.nome_input = QLineEdit()
        layout.addRow(self.nome_label, self.nome_input)

        self.horas_label = QLabel("Horas Trabalhadas:")
        self.horas_input = QLineEdit()
        layout.addRow(self.horas_label, self.horas_input)

        self.valor_label = QLabel("Valor por Hora:")
        self.valor_input = QLineEdit()
        layout.addRow(self.valor_label, self.valor_input)

        self.despesa_label = QLabel("Despesa Adicional (apenas para terceirizados):")
        self.despesa_input = QLineEdit()
        layout.addRow(self.despesa_label, self.despesa_input)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.clicked.connect(self.confirmar)
        layout.addRow(self.confirm_button)

        self.setLayout(layout)

    def confirmar(self):
        nome = self.nome_input.text()
        horas_trabalhadas = self.horas_input.text()
        valor_hora = self.valor_input.text()
        despesa = self.despesa_input.text()
        funcionario = FuncionarioTerceirizado(nome, horas_trabalhadas, valor_hora, despesa)
        lista_funcionarios.append(funcionario.nome)
        lista_funcionarios.append(funcionario.pagamento)
        print(lista_funcionarios)


        pagamento = funcionario.pagamento
        msgBox = QMessageBox()
        msgBox.setText(f"O pagamento é: {pagamento}")
        msgBox.setWindowTitle("Mensagem")
        msgBox.exec()


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