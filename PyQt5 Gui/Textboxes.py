import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.text_box = QLineEdit(self)
        self.button = QPushButton("submit", self)
        self.text_box.setPlaceholderText("Enter your name")
        self.initUI()
        

    def initUI(self):#A method to initialize UI
        self.text_box.setGeometry(10,10,200,40);
        self.text_box.setStyleSheet("font-size:20px; font-family:arial; border:1px solid black; border-radius:5px; ")
        self.button.setGeometry(230,10,100,40);
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.text_box.text();
        print(f"Hello {text}");




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())