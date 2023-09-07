import sys
from PyQt6 import QtWidgets
import UserPw
from getpass import getpass
import mysql.connector 
from PathEnum import PathEnum

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--rootDir', type=str, default="/Users/anujaprakashkolse/Downloads/Project",
					 help='path to the qt ui file')
args = parser.parse_args()

def main():
	with mysql.connector.connect(host = PathEnum.HOSTNAME.value, user = PathEnum.SYSTEMUSERNAME.value, 
		password = PathEnum.SYSTEMPASSWORD.value, database = PathEnum.DATABASENAME.value, buffered = True) as cnx:
		app = QtWidgets.QApplication(sys.argv)
		window = UserPw.UserPw(args.rootDir, cnx)
		window.show()
		app.exec()

if __name__ == "__main__":
	main()