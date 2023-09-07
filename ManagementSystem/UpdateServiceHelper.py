import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import Lease, Insurance, Payment, Service, View
import os
from PathEnum import PathEnum

class UpdateServiceHelper(QWidget):
	def __init__(self, path, cnx, text):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.UPDATESERVICEHELPER.value), self)
		self.submitButton.clicked.connect(self.submit_button)
		self.populateLabel.setText(text)
		self.nextWindow = None
		self.path = path
		self.connection = cnx

	def submit_button(self):
		service_req_id = (self.serviceReqId.toPlainText())
		query = "UPDATE service SET service_status='complete' WHERE service_status='incomplete' AND service_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (service_req_id, ))
		self.connection.commit()
		self.close()