import sys
from PyQt5.QtWidgets import QApplication
from GUI import MainWindow

if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Create an instance of MainWindow
    window = MainWindow()
    # Show the window
    window.show()
    # Run the application's event loop
    sys.exit(app.exec_())