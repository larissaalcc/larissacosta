from typing import Optional
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QMainWindow, QLabel
from PySide6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        