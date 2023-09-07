import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import Lease, Insurance, Payment, Service, View, UpdateServiceHelper
import os
from PathEnum import PathEnum

class Helper(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.HELPER.value), self)
		self.viewService.clicked.connect(self.view_service)
		self.updateService.clicked.connect(self.update_service)
		self.nextWindow = None
		self.path = path
		self.uid = uid
		self.connection = cnx

	def view_service(self):
		query = "SELECT name AS tenant_name, appartment_number, date_request, problem, service_description,service_status FROM service INNER JOIN serviceandhelper ON service.service_id=serviceandhelper.service_id INNER JOIN user ON user.user_id=service.tenant_id WHERE helpprovider_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		ctr = 1
		txt1 = "View service details: "
		text = "(name, apartment_number, reuqest_date, problem, service_description, service_status)\n"
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, txt1)
		self.nextWindow.show()
		
	def update_service(self):
		query = "SELECT name AS tenant_name, appartment_number, date_request, problem, service_description, service_status, service.service_id FROM service INNER JOIN serviceandhelper ON service.service_id=serviceandhelper.service_id INNER JOIN user ON user.user_id=service.tenant_id WHERE helpprovider_id=%s AND service_status='incomplete'"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		ctr = 1
		text = "(name, apartment_number, request_date, problem, service_description, service_status, service request id)\n"
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = UpdateServiceHelper.UpdateServiceHelper(self.path, self.connection, text)
		self.nextWindow.show()
