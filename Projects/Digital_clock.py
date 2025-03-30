import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.text_label = QLabel(self)
        self.time = QTimer(self)
        self.time.timeout.connect(self.update_time) # This feature updates the time in seconds to look ore lively
        self.time.start(1000) #milliseconds to update the time per second
        self.initUI()
        self.update_time()



    def initUI(self):
        self.text_label.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Digital Clock")
        self.setGeometry(400,200,300,100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_label);
        self.text_label.setStyleSheet("font-size:30px; color: green;")
        self.setStyleSheet("background-color:black;")
        

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") #Gets the current time in hrs mins and secs
        self.text_label.setText(current_time) #appending the current time into the label


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())