import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum
import View, DeleteCardDetails, AddCardDetails, PayBill

class CardDetails(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.CARDDETAILS.value), self)
		self.cardDetails.clicked.connect(self.view_card_details)
		self.addCardDetails.clicked.connect(self.add_card_details)
		self.deleteCardDetails.clicked.connect(self.delete_card_details)
		self.payBill.clicked.connect(self.pay_bill)
		self.nextWindow = None
		self.path = path
		self.connection = cnx
		self.uid = uid

	def view_card_details(self):
		get_user_id_db_query = "SELECT * FROM tenantcarddetails WHERE tenant_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(get_user_id_db_query, (self.uid, ))
		result = cursor.fetchall()
		ctr = 1
		text = "(tenantcarddetails_id, tenant_id, card_number, exp_date, security_code)\n"
		text1 = "Card details: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()

	def add_card_details(self):
		self.nextWindow = AddCardDetails.AddCardDetails(self.path, self.connection, self.uid)
		self.nextWindow.show()

	def delete_card_details(self):
		self.nextWindow = DeleteCardDetails.DeleteCardDetails(self.path, self.connection)
		self.nextWindow.show()

	def pay_bill(self):
		get_user_id_db_query = "SELECT * FROM tenantcarddetails WHERE tenant_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(get_user_id_db_query, (self.uid, ))
		result = cursor.fetchall()
		card_id_list = []
		ctr = 1
		text = "(tenantcarddetails_id, tenant_id, card_number, exp_date, security_code)\n"
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
			card_id_list.append(str(row[0]))
		self.nextWindow = PayBill.PayBill(self.path, self.connection, self.uid, text, card_id_list)
		self.nextWindow.show()
