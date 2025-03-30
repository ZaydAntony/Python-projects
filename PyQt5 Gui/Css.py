# learning how to properly work with css

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500);
        self.button1 = QPushButton("#1");
        self.button2 = QPushButton("#2");
        self.button3 = QPushButton("#3");
        self.initUI()

    def initUI(self):
        central_widget =  QWidget()
        self.setCentralWidget(central_widget);
        hbox = QHBoxLayout();
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox);
        self.button1.setObjectName("btn1")
        self.button2.setObjectName("btn2")
        self.button3.setObjectName("btn3")

        # ADVANCED CSS

        self.setStyleSheet("""
            QPushButton{
                        font-size:20px;
                        padding: 15px 55px;
                        margin:20px;
                        }
            QPushButton#btn1{
                        background-color:red;
                        }
            QPushButton#btn2{
                        background-color:green;
                        }
            QPushButton#btn3{
                        background-color:blue;
                        }
            
""")





if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())