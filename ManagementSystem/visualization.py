import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PathEnum import PathEnum
import mysql.connector 

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, rows, columns):
        super(MainWindow, self).__init__()
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(rows, columns)
        toolbar = NavigationToolbar(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

class Visualization(QWidget):
    def __init__(self, cnx):
        super().__init__()
        uic.loadUi(PathEnum.VISUALIZATION.value, self)
        self.helpProviders.clicked.connect(self.help_providers)
        self.tenantsGender.clicked.connect(self.tenants_gender)
        self.highestService.clicked.connect(self.highest_service)
        self.nextWindow = None
        self.connection = cnx
        
    def help_providers(self):
        query = "SELECT role, count(*) FROM user INNER JOIN helpprovider ON user.user_id=helpprovider.helpprovider_id GROUP BY role"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        rows = []
        columns = []
        for row in result:
            rows.append(row[0])
            columns.append(row[1])
        self.nextWindow = MainWindow(rows,columns)
        self.nextWindow.show()
        
    def tenants_gender(self):
        query = "SELECT gender, count(*) FROM user WHERE user_id like 'T%' GROUP BY gender"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        rows = []
        columns = []
        for row in result:
            rows.append(row[0])
            columns.append(row[1])
        self.nextWindow = MainWindow(rows,columns)
        self.nextWindow.show()

    def highest_service(self):
        query = "SELECT problem, count(*) FROM service INNER JOIN user ON service.tenant_id=user.user_id GROUP BY problem"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        rows = []
        columns = []
        for row in result:
            rows.append(row[0])
            columns.append(row[1])
        self.nextWindow = MainWindow(rows,columns)
        self.nextWindow.show()

if __name__ == "__main__":
    with mysql.connector.connect(host = PathEnum.HOSTNAME.value, user = PathEnum.SYSTEMUSERNAME.value, 
        password = PathEnum.SYSTEMPASSWORD.value, database = PathEnum.DATABASENAME.value, buffered = True) as cnx:
        app = QtWidgets.QApplication(sys.argv)
        window = Visualization(cnx)
        window.show()
        app.exec()
    