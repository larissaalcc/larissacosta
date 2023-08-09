
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QMainWindow, QLabel, QCheckBox
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro")
        self.setFixedSize(800,600)
        
        self.label1 = QLabel("Nome:",self)
        self.label1.setGeometry(10,10,80,30)
        
        self.label2 = QLabel("Telefone:",self)
        self.label2.setGeometry(10,50,80,30)
        
        self.label3 = QLabel("Endereço:",self)
        self.label3.setGeometry(10,90,80,30)
        
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(120,10,80,30)
        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(120,50,80,30)
        
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(120,90,80,30)
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()