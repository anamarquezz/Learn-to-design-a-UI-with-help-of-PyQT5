# class inheriting from QWidget

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow


class GUI(QMainWindow):    #inherit from QWidget
    def __init__(self):
        super().__unit__()              # Initialize super class wich creates the window
        self.initUI()                  

    def initUI(self):
        self.setWindowTitle('PYQT23232 GUI')    # Add widgets and change propoerties
        self.resize(400,300)

if __name__ == '__main__':                  # Create application
    app = QApplication(sys.argv)            # Create aplication
    app = GUI()                             # Show the constructed PyQt window
    gui.show()                              # Execute the application    
