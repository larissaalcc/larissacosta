'''class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor + 5 <= self.saldo:  # Considera a taxa de R$ 5,00 para saque
            self.saldo -= (valor + 5)
            print(f"Saque de {valor} realizado. Taxa de R$ 5,00 aplicada. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


# Exemplo de uso
if __name__ == "__main__":
    nome = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    
    conta = ContaBancaria(nome, saldo_inicial)
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar Saldo")
        print("4 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.consultar_saldo()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            '''

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow

# Importe sua classe ContaBancaria aqui
class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}"
        else:
            return "Valor inválido para depósito."

    def sacar(self, valor):
        if valor > 0 and valor + 5 <= self.saldo:  # Considera a taxa de R$ 5,00 para saque
            self.saldo -= (valor + 5)
            return f"Saque de {valor} realizado. Taxa de R$ 5,00 aplicada. Novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente ou valor inválido para saque."

    def consultar_saldo(self):
        return f"Saldo atual: {self.saldo}"

# Importe a classe gerada pelo Qt Designer aqui'''
from contabancaria_ui import Ui_MainWindow

class MinhaAplicacao(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Crie uma instância da classe ContaBancaria
        self.conta = None

        # Conecte os sinais dos botões aos métodos
        self.BotaoCadastrar.clicked.connect(self.realizar_cadastro)
        self.pushButton.clicked.connect(self.ver_saldo)
        self.checkdeposito.stateChanged.connect(self.habilitar_deposito)
        self.checksaque.stateChanged.connect(self.habilitar_saque)
        
        self.habilitar_deposito()  # Por padrão, depósito estará habilitado
        self.habilitar_saque()  # Por padrão, saque estará desabilitado

    def realizar_cadastro(self):
        nome_titular = self.LineEditNome.text()
        saldo_inicial = float(self.LineeditDeposito.text())
        
        self.conta = ContaBancaria(nome_titular, saldo_inicial)
        print("Cadastro realizado!")

    def ver_saldo(self):
        if self.conta:
            saldo = self.conta.consultar_saldo()
            print(saldo)
        else:
            print("Cadastre uma conta primeiro.")

    def habilitar_deposito(self):
        if self.checkdeposito.isChecked():
            self.LineeditDeposito.setEnabled(True)
        else:
            self.LineeditDeposito.setEnabled(False)
            self.LineeditDeposito.clear()

    def habilitar_saque(self):
        if self.checksaque.isChecked():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

if __name__ == "__main__":
    app = QApplication([])
    window = MinhaAplicacao()
    window.show()
    app.exec_()
