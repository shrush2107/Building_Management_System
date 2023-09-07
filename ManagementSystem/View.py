import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum

class View(QWidget):
	def __init__(self, path, displayText, heading):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.VIEW.value), self)
		self.populatedLabel.setText(displayText) 
		self.label.setText(heading)