import sys
from PyQt5.QtWidgets import  QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.label = QLabel( self)
        self.start_btn = QPushButton("Start", self)
        self.stop_btn = QPushButton("Stop", self)
        self.reset_btn = QPushButton("Reset", self)
        self.timer= QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(300,200,400,400)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.stop_btn)
        hbox.addWidget(self.reset_btn)

        vbox.addLayout(hbox);

        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)



        self.setStyleSheet("""
                QPushButton{
                        font-size:15px;
                        padding:15px 75px;
                        background-color:green;
                        }
                QLabel{
                        font-size:30px;
                        font-style:italic;
                        font-weight:bold;
                        background-color:beige;
                        }
                """)

    def start(self):
        self.timer.start(10)# Timer runs as per 1o ms

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.label.setText(self.format_time(self.time))
    def format_time(self,time):
            hours = time.hour()
            mins = time.minute()
            sec = time.second()
            millisec= time.msec() // 10 #integer division by 10 to get only 2 digits

            return f"{hours:02}: {mins:02}: {sec:02}.{millisec:02}";

    def update_display(self):
        self.time = self.time.addMSecs(10) #updating by 10 milliseconds
        self.label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = Stopwatch()
    watch.show()
    sys.exit(app.exec_())