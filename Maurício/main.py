from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QBoxLayout, QDialog, QFrame
import sys 
from contabancaria_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super .__init__()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    app.exec()