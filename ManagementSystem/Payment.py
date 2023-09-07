import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum
import CardDetails, View

class Payment(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__()
		uic.loadUi(os.path.join(path, PathEnum.PAYMENT.value), self)
		self.doneButton.clicked.connect(self.done_button)
		self.backButton.clicked.connect(self.back_button)
		self.checkBillingDetailsButton.clicked.connect(self.check_billing_details_button)
		self.payCurrentBillButton.clicked.connect(self.pay_current)
		self.nextWindow = None
		self.path = path
		self.uid = uid
		self.connection = cnx


	def back_button(self):
		self.close()

	def done_button(self):
		sys.exit()

	def pay_current(self):
		self.nextWindow = CardDetails.CardDetails(self.path, self.connection, self.uid) 
		self.nextWindow.show()


	def check_billing_details_button(self):
		query = "SELECT user.name, lease.appartment_number, lease.rent_amount, rentbill.due_date, rentbill.status FROM user INNER JOIN tenant ON user.user_id=tenant.tenant_id INNER JOIN lease ON tenant.tenant_id=lease.tenant_id INNER JOIN rentbill ON rentbill.tenant_id=tenant.tenant_id WHERE user.user_id=%s";
		with self.connection.cursor() as cursor:
			cursor.execute(query, (self.uid, ))
		result = cursor.fetchall()
		ctr = 1
		text = "(name, apartment_number, rent_amount, due_date, status)\n"
		text1 = "Billing details: "
		for row in result:
			text = text + str(ctr) + ". " + str(row) + "\n"
			ctr += 1
		self.nextWindow = View.View(self.path, text, text1)
		self.nextWindow.show()
		return


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Payment()
	window.show()
	app.exec()