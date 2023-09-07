import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
import os
from PathEnum import PathEnum

class DeleteCardDetails(QWidget):
	def __init__(self, path, cnx):
		super().__init__() 
		uic.loadUi(os.path.join(path, PathEnum.DELETECARDDETAILS.value), self)
		self.submitButton.clicked.connect(self.submit_button)
		self.path = path
		self.connection = cnx

	def submit_button(self):
		id = (self.idInput.toPlainText())
		query = "DELETE FROM tenantcarddetails WHERE tenantcarddetails_id=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(query, (id, ))
		self.connection.commit()
		self.close()
