import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum
import View

class Insurance(QtWidgets.QDialog):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.INSURANCE.value), self)
		self.insuranceDetailsButton.clicked.connect(self.insurance_details_button)
		self.doneButton.clicked.connect(self.done_button)
		self.backButton.clicked.connect(self.back_button)
		self.nextWindow = None
		self.path = path
		self.connection = cnx
		self.uid = uid
		
	def insurance_details_button(self):
		query = "SELECT name, appartment_number, insurance_provider, tenure, insurance.start_date FROM user INNER JOIN tenant ON user.user_id=tenant_id INNER JOIN lease ON tenant.tenant_id=lease.tenant_id INNER JOIN insurance ON insurance.tenant_id=tenant.tenant_id WHERE user_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		text = "(Tenant name, apartment number, Insurance provider, Tenure, Start date)\n"
		text1 = "Insurance details: "
		for row in result:
			text = text + str(row) + "\n"
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def back_button(self):
		self.close()

	def done_button(self):
		sys.exit()