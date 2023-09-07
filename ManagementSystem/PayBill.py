import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum
import ErrorWindow

class PayBill(QWidget):
	def __init__(self, path, cnx, uid, text, card_id_list):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.PAYBILL.value), self)
		self.availableCards.setText(text)
		self.submit.clicked.connect(self.submit_button)
		self.nextWindow = None
		self.path = path
		self.uid = uid
		self.connection = cnx
		self.cardIdList = card_id_list

	def submit_button(self):
		if (self.cardNum.toPlainText() in self.cardIdList):
			try:
				read_query = "SELECT * FROM rentbill WHERE tenant_id =%s ORDER BY due_date DESC LIMIT 1"
				with self.connection.cursor() as cursor:
					cursor.execute(read_query, (self.uid, ))
				result = cursor.fetchall()
				for row in result:
					bill_id = row[0]
				query = "UPDATE rentbill SET status='paid' WHERE bill_id=%s and status='not paid'"
				with self.connection.cursor() as cursor:
					cursor.execute(query, (bill_id, ))
				self.connection.commit()
			except Exception as e:
				print (e)
				self.nextWindow = ErrorWindow.ErrorWindow(self.path)
				self.nextWindow.show()
		else:
			self.nextWindow = ErrorWindow.ErrorWindow(self.path)
			self.nextWindow.show()