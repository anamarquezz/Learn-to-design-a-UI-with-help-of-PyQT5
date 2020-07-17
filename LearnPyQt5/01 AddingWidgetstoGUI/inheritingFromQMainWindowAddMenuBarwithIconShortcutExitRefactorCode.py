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
		self.resize(400,300)				# resize the window(width, height)
		self.add_menus_and_status()

	def add_menus_and_status(self):
		self.statusBar().showMessage('Text in statusbar')

		menubar =self.menuBar()							# create menu bar
		file_menu = menubar.addMenu('File')				# add first menu

		new_icon = QIcon('Icons/new_icon.png')			# create icon
		new_action = QAction(new_icon, 'New', self)		# add actionh to menu
		new_action.setStatusTip('New File')				# update statusBar
		file_menu.addAction(new_action)					# add action to menu

		file_menu.addSeparator()						# add separator line between menu items

		exit_icon = QIcon('../icons/exit_icon.png')		# create icon
		exit_action = QAction(exit_icon,'Exit', self)	# create Exit Action
		exit_action.setStatusTip('Click to exit the application')
		exit_action.triggered.connect(self.close)		# close application when clicked
		exit_action.setShortcut('Ctrl+Q')					# close application when clicked
		file_menu.addAction(exit_action)				# keyboard shortcut, window has focues

if __name__ == '__main__':
	app = QApplication(sys.argv)			# create Application
	gui = GUI()								# create ubstabce if ckass
	gui.show()								# show the constructed OyQt window
	sys.exit(app.exec_())					# execute the application
