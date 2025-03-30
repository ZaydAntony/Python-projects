import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
import string;
import random;


class Encrypt(QWidget):
    def __init__(self):
        super().__init__()
        self.intro = QLabel("Welcome to Encrypt.io", self)
        self.text_box = QLineEdit(self);
        self.encrypt_btn = QPushButton("Encrypt", self)
        self.decrypt_btn = QPushButton("Decrypt", self)
        self.label1 = QLabel("Encrypted txt:")
        self.label2 = QLabel("Decrypted txt:")
        self.result1 = QLabel(self)
        self.result2 = QLabel(self)
        self.chars =" " + string.punctuation + string.digits + string.ascii_letters;
        self.chars=list(self.chars);
        self.key = self.chars.copy();
        random.shuffle(self.key);
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Encrypt Messages")
        self.setGeometry(0,0,500,500)
        vbox = QVBoxLayout()
        vbox.addWidget(self.intro)
        vbox.addWidget(self.text_box)

        hbox =QHBoxLayout()
        hbox.addWidget(self.encrypt_btn)
        hbox.addWidget(self.decrypt_btn)

        gbox= QGridLayout()
        gbox.addWidget(self.label1, 0,0)
        gbox.addWidget(self.label2, 0,1)
        gbox.addWidget(self.result1, 1,0)
        gbox.addWidget(self.result2, 1,1)

        vbox.addLayout(hbox);
        vbox.addLayout(gbox);
        self.setLayout(vbox);
        self.intro.setAlignment(Qt.AlignCenter| Qt.AlignTop)
        self.intro.setStyleSheet("font-size:25px; font-style:italic; text-decoration:underline; font-weight:bold; color:blue; ")
        self.setStyleSheet("background-color:beige;")
        self.label1.setStyleSheet("font-size:15px; font-style:italic; text-decoration:underline; font-weight:bold;")
        self.label2.setStyleSheet("font-size:15px; font-style:italic; text-decoration:underline; font-weight:bold;")
        self.text_box.setStyleSheet("border:0.5px solid black; font-size:20px; padding:15px 75px; border-radius:5px;")
        self.text_box.setPlaceholderText("Enter message")
        self.encrypt_btn.setStyleSheet("padding:10px 15px; background-color:green; color:white; font-size:15px; border-radius:8px; margin:8px; ")
        self.decrypt_btn.setStyleSheet("padding:10px 15px; background-color:black; color:white; font-size:15px; border-radius:8px; margin:8px; ")
        self.result1.setStyleSheet("font-size:20px; font-style:italic; ")
        self.result2.setStyleSheet("font-size:20px; font-style:italic; ")
        self.result1.setAlignment(Qt.AlignCenter)
        self.result2.setAlignment(Qt.AlignCenter)




        self.encrypt_btn.clicked.connect(self.encrypt)
        self.decrypt_btn.clicked.connect(self.decrypt)


    def encrypt(self):
        message = self.text_box.text();
        encrypted_text=" ";
        for letter in message:
            index=self.chars.index(letter);
            encrypted_text += self.key[index];
            self.result1.setText(encrypted_text)

    def decrypt(self):
        encrypted_text=self.text_box.text();
        message = "";
        for letter in encrypted_text:
            index=self.key.index(letter);
            message += self.chars[index];
            self.result2.setText(message)


if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = Encrypt()
    window.show()
    sys.exit(app.exec_())