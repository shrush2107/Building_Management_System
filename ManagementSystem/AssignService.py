import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum

class AssignService(QWidget):
	def __init__(self, path, cnx, text1, text2):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.ASSIGNSERVICE.value), self)
		self.openServices.setText(text1)
		self.helpers.setText(text2)
		self.submit.clicked.connect(self.submit_button)
		self.nextWindow = None
		self.path = path
		self.connection = cnx

	def submit_button(self):
		service_id = (self.serviceId.toPlainText())
		helper_id = (self.helperId.toPlainText())
		query = "INSERT INTO serviceandhelper(service_id, helpprovider_id) VALUES(%s, %s);"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (service_id, helper_id))
		self.connection.commit()
		self.close()