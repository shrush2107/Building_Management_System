import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget
import os
from PathEnum import PathEnum
from datetime import datetime

class RaiseService(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.RAISESERVICE.value), self)
		self.submitButton.clicked.connect(self.submit_button)
		self.path = path
		self.connection = cnx
		self.uid = uid

	def submit_button(self):
		apt_no = (self.aptNo.toPlainText())
		service_desc = (self.serviceDesc.toPlainText())
		if self.householdButton.isChecked():
			problem = "Household Repair"
		elif self.pestButton.isChecked():
			problem = "Pest control"
		else:
			problem = "Plumbing issue"
		query = "INSERT INTO service(tenant_id, date_request, problem, service_description, service_status, appartment_number) values(%s, %s, %s, %s, %s, %s)"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, datetime.now().strftime('%Y-%m-%d'), problem, service_desc, "incomplete", apt_no))
		self.connection.commit()
		self.close()
