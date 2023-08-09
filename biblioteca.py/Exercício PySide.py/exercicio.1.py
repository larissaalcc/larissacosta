from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu programa")
        self.setFixedSize(QSize(600,400))
        self.lbl=QLabel("Hello Word!")
        font=self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment( Qt.AlignCenter | Qt.alignCenter)
        self.setCentralWidget(self.lbl)
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()