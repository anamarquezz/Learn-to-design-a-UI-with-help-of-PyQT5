# class inheriting from QMainWindow
# add menu bar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 


class GUI(QMainWindow): 					#Inheriti from WMainWindow
	def __init__(self):
		super().__init__()					#initialize super class, which creates thw window

		self.initUI()

	def initUI(self):						#set properties and add widfets
		self.setWindowTitle('PyQt5 GUI')	#refer to Window as self
		self.statusBar().showMessage('Text in status bar')

		menubar = self.menuBar()			# Create menu bar
		file_menu = menubar.addMenu('File') # add menu to menu bar

		new_action = QAction('new',self)	# create an action
		file_menu.addAction(new_action)		# add Action to menu 
		new_action.setStatusTip('New File')	# statusBar update

		edit_menu = menubar.addMenu('Edit')	# add a second menu

		self.resize(400,300)				# resize window (Width, height)

if __name__ == '__main__':
	app = QApplication(sys.argv)			# create Application
	gui = GUI()								# create ubstabce if ckass
	gui.show()								# show the constructed OyQt window
	sys.exit(app.exec_())					# execute the application
