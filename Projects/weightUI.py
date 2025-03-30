import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class WeightConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.head = QLabel("Weight Converter", self)
        self.text_box = QLineEdit(self)
        self.text_box.setPlaceholderText("Enter Your Weight");
        self.radio_btn1 = QRadioButton("Kg", self)
        self.radio_btn2 = QRadioButton("Lbs", self)
        self.btn = QPushButton("Convert", self)
        self.result = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weight Converter")
        self.setGeometry(0,0,400,400);
        vbox = QVBoxLayout()
        vbox.addWidget(self.head)
        vbox.addWidget(self.text_box)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.radio_btn1)
        hbox.addWidget(self.radio_btn2)
        vbox.addWidget(self.btn)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.head.setAlignment(Qt.AlignCenter| Qt.AlignTop)
        self.head.setStyleSheet("font-size:20px; font-style:italic; font-weight:bold; text-decoration:underline;")
        self.btn.clicked.connect(self.convert_weight)
        self.result.setStyleSheet("font-size:12px; font-weight:bold; font-style:italic; padding:10px 25px;")
        self.result.setGeometry(0,0,400,40)

        

        self.setStyleSheet("""
                QLineEdit{
                        padding:15px 75px;
                        font-size:18px;
                        border:0.5px solid black;
                        border-radius:15px;
                    }

                QPushButton{
                            padding:15px 50px;
                            font-size:20px;
                            border-radius:8px;
                            background-color:black;
                            color:White;
                            font-style:italic;
                        }

                QRadioButton{
                            font-size:20px;
                            font-style:italic;
                            padding:40px;
                        }
                    """)
        

    
    def convert_weight(self):
        self.weight=float(self.text_box.text())

        try:
            if self.radio_btn1.isChecked():
                converted_weight = self.weight * 2.205 #kgs to pounds
                self.result.setText(f"Your weight in pounds is: {converted_weight:.2f}Lbs")
            elif self.radio_btn2.isChecked():
                converted_weight = self.weight / 2.205 #kgs to pounds
                self.result.setText(f"Your weight Kg is {converted_weight: .2f}Kgs")
        except Exception:
            self.result.setText("Please enter a valid value")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeightConverter()
    window.show()
    sys.exit(app.exec_())