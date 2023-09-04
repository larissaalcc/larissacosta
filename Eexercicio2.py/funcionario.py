import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDialog, QFormLayout, QMessageBox

class Funcionario:
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = int(horas_trabalhadas)
        self.valor_hora = int(valor_hora)
        self.pagamento = (self.horas_trabalhadas * self.valor_hora)

class FuncionarioTerceirizado(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora, despesa_adicional):
        super().__init__(nome, horas_trabalhadas, valor_hora)
        self.despesa_adicional = int(despesa_adicional)
        self.pagamento = (self.valor_hora * self.horas_trabalhadas) + (self.despesa_adicional * 1.1)