from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox, QBoxLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check box")
        self.label = QLabel("Clique e aceite as condições")
        self.ck = QCheckBox("Aceito")
        self.label2 = QLabel()
        layout = QBoxLayout()
        layout.addWidget(self.label)
        layout = QBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    
        
    def state(self,s):
        if s == 2:
            self.label.setText("Nao aceito")
        else:
            self.label2.setText("")
            
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()