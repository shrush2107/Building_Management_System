import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget
import os
from PathEnum import PathEnum
import ErrorWindow

class AddCardDetails(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.ADDCARDDETAILS.value), self)
		self.submitButton.clicked.connect(self.submit_button)
		self.path = path
		self.connection = cnx
		self.uid = uid

	def submit_button(self):
		card_number = (self.cardNumber.toPlainText())
		exp_date = (self.expiryDate.toPlainText())
		security_code = (self.securityCode.toPlainText())
		if self.validation():
			query = "INSERT INTO tenantcarddetails(tenant_id, card_number, exp_date, security_code) VALUES(%s,%s,%s,%s);"
			with self.connection.cursor() as cursor:
				cursor.execute(query, (self.uid, card_number, exp_date, security_code))
			self.connection.commit()
			self.close()
		else:
			self.nextWindow = ErrorWindow.ErrorWindow(self.path)
			self.nextWindow.show()

	def validation(self):
		if ((len(self.cardNumber.toPlainText()) == 16) and (self.cardNumber.toPlainText().isdigit()) and (self.securityCode.toPlainText().isdigit()) and (len(self.securityCode.toPlainText()) == 3)):
			return True
		else:
			return False

