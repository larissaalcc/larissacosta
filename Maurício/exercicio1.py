import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class contaBancaria:
    def __init__(self, numero_conta, titular_conta, deposito_inicial,):
        saldo = 0
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.deposito_inicial = deposito_inicial

class abrindoContaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de conta")
        self.setGeometry(100, 100, 300, 200)

        self.contaUI()

    def contaUI(self):
        layout = QVBoxLayout()

        self.numero_label = QLabel("Número da conta:")
        self.numero_input = QLineEdit()
        layout.addWidget(self.numero_label)
        layout.addWidget(self.numero_input)

        self.nome_label = QLabel("Nome do titular da conta:")
        self.nome_input = QLineEdit()
        layout.addWidget(self.nome_label)
        layout.addWidget(self.nome_input)

        self.deposito_label = QLabel("Depósito Inicial:")
        self.deposito_input = QLineEdit()
        layout.addWidget(self.deposito_label)
        layout.addWidget(self.deposito_input)

        self.criar_botao = QPushButton("Criar conta")
        self.criar_botao.clicked.connect(self.criar_conta)
        layout.addWidget(self.criar_botao)

        self.criar_botaoSaque = QPushButton("Saque")
        self.criar_botaoSaque.clicked.connect(self.saque)
        layout.addWidget(self.criar_botaoSaque)

        self.saque_label = QLabel("Valor para saque:")
        self.saque_input = QLineEdit()
        layout.addWidget(self.saque_label)
        layout.addWidget(self.saque_input)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def saque(self):
        print("Qualquer saque é acompanhado com uma taxa de R$5,00")
        saldo = (int(self.deposito_input)) - (int(self.saque_input)) - 5
        print (f"Seu saldo é de",saldo)
        print("Saque efetuado com sucesso!")

    def criar_conta(self):
    
        numero_conta = self.numero_input.text()
        titular_conta = self.nome_input.text()
        deposito_inicial = self.deposito_input.text()

        conta = contaBancaria(numero_conta, titular_conta, deposito_inicial)
        print("Conta criada:")
        print("Numero da conta:", conta.numero_conta)
        print("Titular da conta:", conta.titular_conta)
        print("Saldo Inicial:", conta.deposito_inicial)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = abrindoContaWindow()
    window.show()
    sys.exit(app.exec())