# class inheriting from QWidget

import sys 
from PyQt5.QtWidgets import QApplication, QWidget


class GUI():           #inherit from QWidget
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.win = QWidget()                        #   create window
        self.win.setWindowTitle('PyQt5 GUI')        # add widgets and change properties

if __name__ == '__main__':
    app = QApplication(sys.argv)                    # Create Application
    gui = GUI()                                     # Create instance of class
    gui.win.show()                                  # show the constructed PyQt window
    sys.exit(app.exec_())                           # execute the application