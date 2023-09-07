import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
from PathEnum import PathEnum
import os

class CreatePassword(QWidget):
	def __init__(self, path, cnx):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.CREATEPW.value), self)
		self.submit.clicked.connect(self.submit_button)
		self.nextWindow = None
		self.path = path
		self.connection = cnx
		

	def submit_button(self):
		username = (self.userName.toPlainText())
		password = (self.password.toPlainText())
		query = "UPDATE user SET userpassword=%s WHERE usercred=%s"
		try:
			with self.connection.cursor() as cursor:
				cursor.execute(query, (password, username))
			self.connection.commit()
			self.close()
		except Exception as e:
			self.nextWindow = ErrorWindow.ErrorWindow(self.path)
			self.nextWindow.show()