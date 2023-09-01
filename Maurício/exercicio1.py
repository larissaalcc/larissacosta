import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class contaBancaria:
    def __init__(self, numero_conta, titular_conta, deposito_inicial,):
        self.numero_conta = int(numero_conta)
        self.titular_conta = titular_conta
        self.__deposito_inicial = float(deposito_inicial)
        
    def get_saldo(self):
        return self.__deposito_inicial
    
    def get_saldoDeposito(self):
        return self.__deposito_inicial
    

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
        
        self.criar_botaoDeposito = QPushButton('Depositar')
        self.criar_botaoDeposito.clicked.connect(self.deposito)
        layout.addWidget(self.criar_botaoDeposito)
        
        
        
        self.saque_label = QLabel("Valor para saque:")
        self.saque_input = QLineEdit()
        layout.addWidget(self.saque_label)
        layout.addWidget(self.saque_input)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def deposito(self):
        
        conta_saldo = self.conta.get_saldo()
        deposito = float(self.deposito_input.text())
        saldo = (conta_saldo) + (deposito) 
        print (f"Seu saldo é de",saldo)
        print("Saque efetuado com sucesso!")
        
        
        
    def calc_deposito(self):
        

 
        

        print("Qualquer saque é acompanhado com uma taxa de R$5,00")
        conta_saldo = self.conta.get_saldo()
        saque = float(self.saque_input())
        saldo = (conta_saldo) - (saque) - 5
        

    def criar_conta(self):
        if self.deposito_input.text() == "":
            numero_conta = self.numero_input.text()
            titular_conta = self.nome_input.text()
            deposito_inicial = 0

            self.conta = contaBancaria(numero_conta, titular_conta, deposito_inicial)
            print("Conta criada:")
            print("Numero da conta:", self.conta.numero_conta)
            print("Titular da conta:", self.conta.titular_conta)
            print("Saldo Inicial:", self.conta.get_saldo())
            
        else:
            numero_conta = self.numero_input.text()
            titular_conta = self.nome_input.text()
            deposito_inicial = self.deposito_input.text()
            self.conta = contaBancaria(numero_conta, titular_conta, deposito_inicial)
            print("Conta criada:")
            print("Numero da conta:", self.conta.numero_conta)
            print("Titular da conta:", self.conta.titular_conta)
            print("Saldo Inicial:", self.conta.get_saldo())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = abrindoContaWindow()
    window.show()
    sys.exit(app.exec())
     