import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check boxes")
        self.setGeometry(500,200,500,500)
        self.checkbox = QCheckBox("Do you like pizza ?", self)
        self.initUI()


    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("Font-size:20px;")
        self.checkbox.stateChanged.connect(self.checkbox_changed);

    def checkbox_changed(self,state):
        if state == Qt.Checked:
            print("you like pizza");
        else:
            print("Fr Githeri is better 😂")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


