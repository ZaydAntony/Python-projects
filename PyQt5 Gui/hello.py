# Getting user input and displaying  it on th ui

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class Display(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_box = QLineEdit(self)
        self.submit = QPushButton("submit", self)
        self.display = QLabel(self)
        self.initUI();

    def initUI(self):
        self.setWindowTitle("Hello page")
        self.setGeometry(0,0,400,400)
        self.text_box.setStyleSheet("font-size:20px; font-family:arial; margin:10px;")
        self.text_box.setGeometry(10,10,150,50);
        self.submit.setGeometry(150,20,100,30);
        self.display.setGeometry(0,60,100,100);
        self.submit.clicked.connect(self.update_display)
    
    def update_display(self):
        text = self.text_box.text();
        self.display.setText(text);
        






if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = Display()
    window.show()
    sys.exit(app.exec_())