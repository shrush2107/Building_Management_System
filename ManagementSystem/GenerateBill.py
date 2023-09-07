import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum

class GenerateBill(QWidget):
	def __init__(self, path, cnx, uid):
		super().__init__() 
		uic.loadUi(os.path.join(path, PathEnum.GENERATEBILL.value), self)
		self.submitButton.clicked.connect(self.submit_button)
		self.path = path
		self.connection = cnx
		self.uid = uid

	def submit_button(self):
		due_date = (self.dueDate.toPlainText())
		tenant_id = (self.tenantId.toPlainText())
		args = [self.uid, tenant_id, due_date]
		with self.connection.cursor() as cursor:
			cursor.callproc('generatebill', args)
		self.close()