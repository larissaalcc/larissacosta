
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QMainWindow, QLabel, QFrame, QBoxLayout 
from PySide6.QtCore import Qt, QSize 
from PySide6.QtGui import QPixmap 
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        
    def trabalho(self):
        
        self.setWindowTitle("Pokémon")
        self.setGeometry(100,100,300,150)
        
        self.button_pokemon1 = QPushButton ("Pokémon 1")
        self.button_pokemon2 = QPushButton ("Pokémon 2")
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(600,400)
        self.image_frame.setLayout(QBoxLayout())
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.alignCenter)
        self.image_frame.layout().addWidget(self.image_label)
        
        self.button_pokemon1.clicked.connect(self.display_pikachu)
        self.button_pokemon2.clicked.connect(self.display_dragao)
        
        layout = QBoxLayout()
        layout.addWidget(self.button_pokemon1)
        layout.addWidget(self.button_pokemon2)
        layout.addWidget(self.image_frame)
        
        self.setLayout(layout)
        
    def display_pikachu(self):
        pixmap = QPixmap("pikachu.jpg")
        self.image(pixmap)
        
    def display_dragao(self):
        pixmap = QPixmap("pokemon_dragao.jpg")
        self.image(pixmap)
        
    def image(self,pixmap):
        scale_pixmap = pixmap.scaled(600,400,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scale_pixmap)
        
           
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
       