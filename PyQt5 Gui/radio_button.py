#working with radio buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio's")
        self.setGeometry(0,0,500,500)
        self.radio_btn1 = QRadioButton("visa", self);
        self.radio_btn2 = QRadioButton("Mpesa", self);
        self.radio_btn3 = QRadioButton("Master_card", self);
        self.means_1 = QRadioButton("in-store",self);
        self.means_2 = QRadioButton("Online", self);
        self.mode= QButtonGroup(self)
        self.means= QButtonGroup(self)

        self.initUI()


    def initUI(self):
        self.radio_btn1.setGeometry(0,0,300,50)
        self.radio_btn2.setGeometry(0,50,300,50)
        self.radio_btn3.setGeometry(0,100,300,50)
        self.means_1.setGeometry(0,150,300,50)
        self.means_2.setGeometry(0,200,300,50)

        #grouping
        self.means.addButton(self.means_1)
        self.means.addButton(self.means_2)

        #functionality
        self.radio_btn1.toggled.connect(self.toggle)
        self.radio_btn2.toggled.connect(self.toggle)
        self.radio_btn3.toggled.connect(self.toggle)
        self.means_1.toggled.connect(self.toggle)
        self.means_2.toggled.connect(self.toggle)
        




        self.setStyleSheet("QRadioButton{"
                            "font-size:20px;"
                            "padding:10px;"
                            "}")

    def toggle(self):
        radio_button = self.sender();
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
