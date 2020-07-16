#structure of Qt5 GUIs

 # win.resize(400,300)set window size: width, height

'''
# Imports
import sys
from PyQt5.QtWidgets import *

# Create Application
app = QApplication(sys.argv)

# Create Window
win = QWidget()

# Add widgets and change properties
win.setWindowTitle('PyQt5 GUI')

# show the constructed Qt window
#win.show()

#app.exec_()  Qt exec_ ends with an underscore
# app.exce()  exec is a python keyword
sys.exit(app.exec_()) # cleanly exit on exception

'''