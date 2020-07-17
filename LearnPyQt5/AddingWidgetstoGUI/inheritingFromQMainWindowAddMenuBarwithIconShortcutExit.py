# class inheriting from QMainWindow
# add menu bar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
from PyQt5.QtGui import QIcon

class GUI(QMainWindow): 					#Inheriti from WMainWindow
	def __init__(self):
		super().__init__()					#initialize super class, which creates thw window

		self.initUI()

	def initUI(self):						#set properties and add widfets
		self.setWindowTitle('PyQt5 GUI')	#refer to Window as self
		self.statusBar().showMessage('Text in status bar')

		menubar = self.menuBar()			# Create menu bar
		file_menu = menubar.addMenu('File') # add menu to menu bar
		new_icon = QIcon('icons/new_icon.png') #create icon
		new_action = QAction(new_icon,'New',self)	# add icon to menu

		file_menu.addAction(new_action)		# add Action to menu 
		new_action.setStatusTip('New File')	# statusBar update

		file_menu.addSeparator()			# add separator line between menu items

		exit_icon = QIcon('icons/exit_icon.png')	 #create icon
		exit_action = QAction(exit_icon,'Exit',self)	#add icon and create action		
		exit_action.setStatusTip('Click to Exit the application')	# statusBar update

		exit_action.triggered.connect(self.close)	# close application when clicked
		exit_action.setShortcut('Ctrl+Q')			# keyboard shortcut to close application

		file_menu.addAction(exit_action)
		
		#-----------------------------------------
		edit_menu = menubar.addMenu('Edit')	# add a second menu

		self.resize(400,300)				# resize window (Width, height)

if __name__ == '__main__':
	app = QApplication(sys.argv)			# create Application
	gui = GUI()								# create ubstabce if ckass
	gui.show()								# show the constructed OyQt window
	sys.exit(app.exec_())					# execute the application
