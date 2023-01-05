import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # Create the widgets
        self.setGeometry(100, 100, 600, 100) #set window size
        self.label = QLabel("Generate Password", self)
        self.line_edit = QLineEdit(self)
        self.generate_button = QPushButton("Generate", self)
        self.clean_button = QPushButton("Clean", self)

        # Set up the layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.clean_button)
        self.setLayout(layout)

        # Connect the buttons to the slots
        self.generate_button.clicked.connect(self.generate)
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
        gen_password = shuffle(self.password)
        self.label.setText("Generated Password:")
        self.line_edit.setText(gen_password)

    def clean(self):
        self.password = ""
        self.label.setText("Generate Password:")
        self.line_edit.setText(self.password)