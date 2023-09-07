import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
from PathEnum import PathEnum
import os
import Tenant, BuildingManager, LeasingManager, Helper, NewCreds

class UserPw(QWidget):
	def __init__(self, path, cnx):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.USERPW.value), self)
		self.submitButton.clicked.connect(self.ok_button)
		self.nextWindow = None
		self.path = path
		self.connection = cnx
		

	def ok_button(self):
		userName = (self.userName.toPlainText())
		password = (self.password.toPlainText())
		get_user_id_db_query = "SELECT user_id FROM user WHERE usercred=%s AND userpassword=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(get_user_id_db_query, (userName, password))
		result = cursor.fetchall()
		user_id = None
		for row in result:
			user_id = (row[0])
		if user_id is None:
			self.nextWindow = NewCreds.NewCreds(self.path, self.connection)
			self.nextWindow.show()
		elif "BM" in user_id:
			self.nextWindow = BuildingManager.BuildingManager(self.path, self.connection, user_id)
			self.nextWindow.show()
		elif "LM" in user_id:
			self.nextWindow = LeasingManager.LeasingManager(self.path, self.connection, user_id)
			self.nextWindow.show()
		elif "T" in user_id:
			self.nextWindow = Tenant.Tenant(self.path, self.connection, user_id)
			self.nextWindow.show()
		elif "HP" in user_id:
			self.nextWindow = Helper.Helper(self.path, self.connection, user_id)
			self.nextWindow.show()
		self.close()