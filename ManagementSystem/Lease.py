import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum
import View

class Lease(QWidget):
	def __init__(self, path, conx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.LEASE.value), self)
		self.leaseDetailsButton.clicked.connect(self.lease_details_button)
		self.doneButton.clicked.connect(self.done_button)
		self.backButton.clicked.connect(self.back_button)
		self.path = path
		self.nextWindow = None
		self.connection = conx
		self.uid = uid
		

	def lease_details_button(self):
		query = "SELECT name, start_date, end_date, rent_amount, appartment_number FROM user INNER JOIN leasingmanager ON user.user_id=leasingmanager.lmanager_id INNER JOIN lease ON lease.lmanager_id=leasingmanager.lmanager_id WHERE tenant_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		text = "(Leasing Manager name, Start date, End date, Rent amount, Apartment number)\n"
		text1 = "Leasing details: "
		for row in result:
			text = text + str(row) + "\n"
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def back_button(self):
		self.close()

	def done_button(self):
		sys.exit()