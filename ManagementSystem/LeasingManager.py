import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import Lease, Insurance, Payment, Service, GenerateBill
import os
from PathEnum import PathEnum
import View

class LeasingManager(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.LEASINGMANAGER.value), self)
		self.viewtenants.clicked.connect(self.view_tenants)
		self.generateBill.clicked.connect(self.generate_bill)
		self.nextWindow = None
		self.path = path
		self.uid = uid
		self.connection = cnx

	def view_tenants(self):
		query = "SELECT tenant.tenant_id, name, gender, phone_number, appartment_number, start_date, end_date, rent_amount FROM tenant INNER JOIN lease ON tenant.tenant_id=lease.tenant_id INNER JOIN user ON user.user_id=tenant.tenant_id WHERE lmanager_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		ctr = 1
		text = "(tenant_id, name, gender, phone_number, apartment_number, start_date, end_date, rent_amount)\n"
		text1 = "Current tenants: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()
		
	def generate_bill(self):
		self.nextWindow = GenerateBill.GenerateBill(self.path, self.connection, self.uid)
		self.nextWindow.show()
	