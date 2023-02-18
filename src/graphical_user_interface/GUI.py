from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from password_generator import passwordGenerator
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

    # Generate Password    
    def generate(self):
        self.label.setText("Generated Password: ")
        # call and catch generated password with function in passwordGenerator
        self.gen_password = passwordGenerator.generate()
        self.gen_label.setText(self.gen_password)
        self.gen_label.show()
        return self.gen_password

    # Delete generated password
    def clean(self):
        self.label.setText("Generate Password: ")
        password = ""
        self.gen_label.setText(password)
        return self.gen_label.hide()
    
    # Copy to clipboard generated password
    def copy(self):
        copy_password = self.gen_password
        #to copy generated password to clipboard
        return pyperclip.copy(copy_password)
        