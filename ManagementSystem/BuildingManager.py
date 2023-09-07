import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import Lease, Insurance, Payment, Service, View, AssignService
import os
from PathEnum import PathEnum

class BuildingManager(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.BUILDINGMANAGER.value), self)
		self.viewTenants.clicked.connect(self.view_tenants)
		self.viewLeasingManagers.clicked.connect(self.view_leasing)
		self.viewServiceRequests.clicked.connect(self.view_service_req)
		self.assignService.clicked.connect(self.assign_service)
		self.nextWindow = None
		self.path = path
		self.uid = uid
		self.connection = cnx

	def view_tenants(self):
		query = "SELECT * FROM user WHERE user_id LIKE 'T%'"
		with self.connection.cursor() as cursor:
			cursor.execute(query)
		result = cursor.fetchall()
		ctr = 1
		text = "(tenant_id, name, gender, phone_number, apartment_number, start_date, end_date, rent_amount)\n"
		text1 = "Current tenants: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def view_leasing(self):
		query = "SELECT * FROM user WHERE user_id LIKE 'LM%'"
		with self.connection.cursor() as cursor:
			cursor.execute(query)
		result = cursor.fetchall()
		ctr = 1
		text = "(tenant_id, name, gender, phone_number, apartment_number, start_date, end_date, rent_amount)\n"
		text1 = "Current leasing managers: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def view_service_req(self):
		query = "SELECT * FROM user WHERE user_id LIKE 'HP%'"
		with self.connection.cursor() as cursor:
			cursor.execute(query)
		result = cursor.fetchall()
		ctr = 1
		text = "(tenant_id, name, gender, phone_number, apartment_number, start_date, end_date, rent_amount)\n"
		text1 = "Current helper partners: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def assign_service(self):
		query = "SELECT * FROM service wHERE service_status='incomplete'"
		with self.connection.cursor() as cursor:
			cursor.execute(query)
		result = cursor.fetchall()
		ctr = 1
		text = "service_id, tenant_id, date, problem, description, status, apartment_number\n"
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		query = "SELECT * FROM helpprovider"
		with self.connection.cursor() as cursor:
			cursor.execute(query)
		result = cursor.fetchall()
		ctr = 1
		text1 = "help_provider_id, address, role\n"
		for row in result:
			text1 = text1 + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = AssignService.AssignService(self.path, self.connection, text, text1) 
		self.nextWindow.show()