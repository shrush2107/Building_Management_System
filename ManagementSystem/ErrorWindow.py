import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
from PathEnum import PathEnum
import os

class ErrorWindow(QWidget):
	def __init__(self, path):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.ERROR.value), self)
		self.pushButton.clicked.connect(self.push_button)

	def push_button(self):
		self.close()