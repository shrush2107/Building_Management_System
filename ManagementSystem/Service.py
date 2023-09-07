import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum
import View, RaiseService

class Service(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.SERVICE.value), self)
		self.checkServiceButton.clicked.connect(self.check_service)
		self.raiseServiceButton.clicked.connect(self.raise_service)
		self.doneButton.clicked.connect(self.done_button)
		self.backButton.clicked.connect(self.back_button)
		self.nextWindow = None
		self.path = path
		self.uid = uid
		self.connection = cnx
		

	def check_service(self):
		query = "SELECT * FROM service WHERE tenant_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		ctr = 1
		text = "(tenant_id, date_request, problem, service_description, service_status, appartment_number)\n"
		text1 = "Service requests: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def raise_service(self):
		self.nextWindow = RaiseService.RaiseService(self.path, self.connection, self.uid)
		self.nextWindow.show()

	def back_button(self):
		self.close()

	def done_button(self):
		sys.exit()