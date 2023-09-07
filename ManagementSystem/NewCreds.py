import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
from PathEnum import PathEnum
import os
import CreatePassword, NewUser

class NewCreds(QWidget):
	def __init__(self, path, cnx):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.NEWCREDS.value), self)
		self.newUser.clicked.connect(self.new_user)
		self.forgotPassword.clicked.connect(self.forgot_password)
		self.nextWindow = None
		self.path = path
		self.connection = cnx
		

	def new_user(self):
		self.nextWindow = NewUser.NewUser(self.path, self.connection)
		self.nextWindow.show()

	def forgot_password(self):
		self.nextWindow = CreatePassword.CreatePassword(self.path, self.connection)
		self.nextWindow.show()