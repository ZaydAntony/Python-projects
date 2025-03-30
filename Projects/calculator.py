import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton,QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(0,0,500,500)
        self.display_box = QLineEdit(self);
        self.display_box.setReadOnly(True)
        self.buttons = [ "1","2","3","4",
                        "5","6","7","8",
                        "9","0","=", "+","-","/","*","C"
                        ];
        self.initUI()


    def initUI(self):
        central_widget =  QWidget()
        self.setCentralWidget(central_widget);


        gbox = QGridLayout()
        gbox.addWidget(self.display_box, 0, 0, 1, 4)
        row, col = 1,0
        for button in self.buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.on_click)
            gbox.addWidget(btn,row,col)

            col +=1
            if  col >3:
                col= 0
                row += 1
            central_widget.setLayout(gbox);

    def on_click(self):
            btn_txt = self.sender().text()
            current = self.display_box.text()

            if btn_txt == "C":
                # Clear the display box
                self.display_box.clear()
            elif btn_txt == "=":
                # Evaluate the expression
                try:
                    answer = str(eval(current))
                    self.display_box.setText(answer)
                except Exception as e:
                    self.display_box.setText("Error")
            else:
                # Append the button text to the current display
                new = current + btn_txt
                self.display_box.setText(new)
                    




            self.setStyleSheet("""
                QPushButton{
                    width:50px;
                    height:50px;
                    border-radius:25px;
                    color:white;
                    background-color:#45a049;
                    font-size:16px;
                
                    }
                QLineEdit {
                            background-color: #f0f0f0;  
                            border: 2px solid #45a049;   
                            border-radius: 10px;
                            padding: 10px;
                            font-size: 18px;
                            color: #333;
                            text-align: right;
                        }
                    """)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())