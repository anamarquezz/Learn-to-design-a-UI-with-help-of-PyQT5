
# Imports
# Structure of PyQt5 GUIs
import sys
from PyQt5.QtWidgets import QApplication, QWidget 
  
  
class GUI():
    def __init__(self): 
                    
        self.initUI()
 
#          
    def initUI(self):   
        self.win = QWidget()                    # create Window
        self.win.setWindowTitle('PyQt5 GUI inheri')    # add widgets and change properties
#  
#  
if __name__ == '__main__':     
    app = QApplication(sys.argv)        # create Application     
    gui = GUI()                         # create instance of class
    gui.win.show()                      # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application