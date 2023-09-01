from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLabel
from PySide6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Localizar o CEP")
        self.setFixedSize(600,400)





app = QApplication()
w = MainWindow()
w.show()
app.exec_()