import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
from PathEnum import PathEnum
import os
import CreatePassword, NewUser, ErrorWindow

class NewUser(QWidget):
	def __init__(self, path, cnx):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.NEWUSER.value), self)
		self.submit.clicked.connect(self.submit_button)
		self.nextWindow = None
		self.path = path
		self.connection = cnx
		

	def submit_button(self):
		userName = (self.userName.toPlainText())
		password = (self.password.toPlainText())
		name = (self.name.toPlainText())
		phone = (self.phoneNum.toPlainText())
		nationality = (self.nationality.toPlainText())
		gender = (self.gender.toPlainText())
		dob = (self.dob.selectedDate().toString("yyyy-MM-dd"))
		if self.validation():
			insert_query = "INSERT INTO user(user_id, name, gender, usercred,userpassword, date_of_birth, phone_number, nationality) values(%s, %s, %s, %s, %s, %s, %s, %s)"
			insert_query_1 = "INSERT INTO tenant(tenant_id) values(%s)"
			try:
				with self.connection.cursor() as cursor:
					cursor.execute(insert_query, ("T25", name, gender, userName, password, dob, phone, nationality))
					cursor.execute(insert_query_1, ("T25", ))
				self.connection.commit()
				self.close()
			except Exception as e:
				self.nextWindow = ErrorWindow.ErrorWindow(self.path)
				self.nextWindow.show()
		else:
			self.nextWindow = ErrorWindow.ErrorWindow(self.path)
			self.nextWindow.show()
		

	def validation(self):
		if (all(x.isalpha() or x.isspace() for x in self.name.toPlainText())) and (self.phoneNum.toPlainText().isdigit()) and (self.nationality.toPlainText().isalpha()) and (self.gender.toPlainText() in ["Male", "Female"]) and (self.dob.selectedDate().toString("yyyy-MM-dd") != ""):
			return True
		return False