

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PySide6.QtCore import QSize
import sys
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercício 2")
        self.button= QPushButton("Botão", self)
        self.button.setGeometry(190,10,100,70)
        self.result_label= QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        self.button.clicked.connect(self.Imprimir)
        
    def Imprimir(self):
        numero=4
        if numero % 2==0:
            self.result_label.setText(f"O número informado foi o número {numero}, e é par")
        else:
            self.result_label.setText(f"O número informado foi o número {numero}, e é ímpar")

app= QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()
            