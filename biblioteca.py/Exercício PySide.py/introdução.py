from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow 
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hello World!!!")
		button = QPushButton("Jho soy um butão")
		self.setCentralWidget(button)
		button.clicked.connect(self.imprimir)
	def imprimir(self):
		print("Larissa")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()