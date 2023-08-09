
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QDialog
from PySide6.QtGui import QPixmap

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(800,400)
        
        self.button = QPushButton("Abrir janela secundária",self)
        self.button.clicked.connect(self.open_secondary_window)
        self.button.setGeometry(100,100,500,100)
        
    def open_secondary_window(self):
        self.secondary_window = SecondaryWindow()
        self.secondary_window.show()

class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Janela Secundária")
        self.setGeometry(200,200,500,300)
        
        layout = QVBoxLayout()
        
        label = QLabel("yuri alberto lindo")
        layout.addWidget(label)
        
        image_label = QLabel(self)
        pixmap = QPixmap("yurilindo.jpg")
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)
        
        close_button = QPushButton("Fechar",self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
        
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()