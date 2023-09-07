import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import Lease, Insurance, Payment, Service
import os
from PathEnum import PathEnum

class Tenant(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.TENANT.value), self)
		self.connection = cnx
		query = "SELECT name, gender, date_of_birth, phone_number, nationality, rent_amount, appartment_number FROM user INNER JOIN tenant ON user.user_id=tenant_id INNER JOIN lease ON tenant.tenant_id=lease.tenant_id WHERE user_id=%s";
		with self.connection.cursor() as cursor:
			cursor.execute(query, (uid, ))
		result = cursor.fetchall()
		if len(result) == 0:
			query = "SELECT name, gender, date_of_birth, phone_number, nationality FROM user WHERE user_id=%s";
			with self.connection.cursor() as cursor:
				cursor.execute(query, (uid, ))
			result = cursor.fetchall()
			self.paymentButton.setEnabled(False)
			self.manageLeaseButton.setEnabled(False)
			self.serviceReqButton.setEnabled(False)
			self.insuranceButton.setEnabled(False)
			for row in result:
				self.monthlyBillingLabel.setText("Not available")
				self.securityDepositLabel.setText(str(row[3]))
				self.aptNumberLabel.setText("Not available")
				self.nationalityLabel.setText(str(row[4]))
				self.ssnLabel.setText(str(row[1]))
				self.nameLabel.setText(str(row[0]))
				self.dob.setText(str(row[2]))
		else:
			self.paymentButton.clicked.connect(self.payment_button)
			self.manageLeaseButton.clicked.connect(self.manage_lease_button)
			self.serviceReqButton.clicked.connect(self.service_request_button)
			self.insuranceButton.clicked.connect(self.insurance_button)
			for row in result:
				self.monthlyBillingLabel.setText(str(row[5]))
				self.securityDepositLabel.setText(str(row[3]))
				self.aptNumberLabel.setText(str(row[6]))
				self.nationalityLabel.setText(str(row[4]))
				self.ssnLabel.setText(str(row[1]))
				self.nameLabel.setText(str(row[0]))
				self.dob.setText(str(row[2]))
		self.nextWindow = None
		self.path = path
		self.uid = uid

	def payment_button(self):
		self.nextWindow = Payment.Payment(self.path, self.connection, self.uid)
		self.nextWindow.show()
		return

	def service_request_button(self):
		self.nextWindow = Service.Service(self.path, self.connection, self.uid) 
		self.nextWindow.show()

	def insurance_button(self):
		self.nextWindow = Insurance.Insurance(self.path, self.connection, self.uid) 
		self.nextWindow.show()

	def manage_lease_button(self):
		self.nextWindow = Lease.Lease(self.path, self.connection, self.uid)
		self.nextWindow.show()