# class inheriting from QMainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class GUI(QMainWindow):
	def __init__(self):		#inherit from QMainWindow
		super().__init__()	#initialize super class, qich creates the window

		self.initUI()		#refer to a window as self

	def initUI(self):
		self.setWindowTitle('PyQt5 GUI') # add widgets and change properties
		self.resize(400,300)

		self.statusBar().showMessage('Text in statusbar')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUI()
	gui.show()
	sys.exit(app.exec_())