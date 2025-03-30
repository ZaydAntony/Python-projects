# working with buttons
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Push Buttons")
        self.setGeometry(300,200,500,500)
        self.button = QPushButton("Click me 🤗",self)
        self.label=QLabel("Hello", self)
        self.initUI()
        

    def initUI(self):
        
        self.button.setGeometry(250, 150, 120, 80)
        self.button.setStyleSheet("Text-align:center; font-size:20px;")
        self.button.clicked.connect(self.onclick)
        self.label.setGeometry(0,0,200,200)
        self.label.setStyleSheet("font-size:20px");

    def onclick(self):
        self.button.setText("Clicked 😎")
        self.label.setText("Goodbye");

if __name__ == "__main__":
    app = QApplication(sys.argv) # future proofing
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # preventing it form closing abruptly