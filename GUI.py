import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
import pyperclip

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # Create the widgets
        self.setGeometry(100, 100, 600, 100) #set window size
        self.label = QLabel("Generate Password:", self)
        self.gen_label = QLabel(self)
        self.gen_label.hide()
        self.generate_button = QPushButton("Generate", self)
        self.copy_button = QPushButton("Copy to Clipboard", self)
        self.clean_button = QPushButton("Clean", self)

        # Set up the layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.gen_label)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.clean_button)
        self.setLayout(layout)

        # Connect the buttons to the slots
        self.generate_button.clicked.connect(self.generate)
        self.copy_button.clicked.connect(self.copy)
        self.clean_button.clicked.connect(self.clean)

    def generate(self):
        # https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf (ASCII table)
        # Generate a random Uppercase letter (based on ASCII code)
        uppercaseLetter1 = chr(random.randint(65, 90))
        # Generate a random Uppercase letter (based on ASCII code)
        uppercaseLetter2 = chr(random.randint(65, 90))
        # Generate a random lowercase letter (based on ASCII code)
        lowercaseLetter1 = chr(random.randint(97, 122))
        # Generate a random lowercase letter (based on ASCII code)
        lowercaseLetter2 = chr(random.randint(97, 122))
        # Generate a random number (based on ASCII code)
        digit1 = chr(random.randint(48, 57))
        # Generate a random number letter (based on ASCII code)
        digit2 = chr(random.randint(48, 57))
        # Generate a random punctuation sign (based on ASCII code)
        punctuationSign1 = chr(random.randint(33, 47))
        # Generate a random punctuation sign (based on ASCII code)
        punctuationSign2 = chr(random.randint(33, 47))

        # Generate password using all the characters, in random order
        self.password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + \
                        lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + \
                        punctuationSign2

        def shuffle(password):
            password = list(password)
            random.shuffle(password)
            return ''.join(password)

        # Shuffle the characters in the password
        self.gen_password = shuffle(self.password)
        self.label.setText("Generated Password: ")
        self.gen_label.setText(self.gen_password)
        #show gen_label, creates new line for generated password
        self.gen_label.show()


    def clean(self):
        self.label.setText("Generate Password:")
        password = ""
        self.gen_label.setText(password)
        self.gen_label.hide()

    def copy(self):
        copy_password = self.gen_password
        #to copy generated password to clipboard
        pyperclip.copy(copy_password)
