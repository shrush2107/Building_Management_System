# Building Management System

## Table of Contents
1. [Original Proposal](#original-proposal)
2. [Technical Description](#technical-description)
3. [Commands Used](#commands-used)

## 1. Original Proposal
This project proposes a Building Management System (BMS) to facilitate and streamline day-to-day activities related to building management. The system would handle tenant interactions and building management services. Tenants could use the system to submit account requests, pay rent, register complaints, request services, and utilize amenities. Building management responsibilities included service assignment to tenants, building maintenance, and management of amenities like parking spaces, laundry facilities, and vending machines. The property management aspect allowed viewing tenant details, such as biographic data, lease dates, the number of people on the lease, and rent details. Service providers could access tenant flat details, complaints, service requests, and their statuses. The admin had full control, including user management and billing responsibilities. The project used Python for both frontend and backend development, leveraging libraries like Tkinter, PyQt5, Matplotlib, Pandas, NumPy, and Seaborn for visualization.

### Modules Proposed:
- **Tenant:**
  - Raise service request
  - Make payment
  - Reserve amenity
  - Manage insurance
  - Manage lease

- **Management:**
  - Assign service request
  - Manage amenities
  - Create/delete users
  - Manage the building

## 2. Technical Description
There is Python-based GUI application that accepts user credentials in the initial window. Based on the user type, the application performs various operations, as depicted in the activity diagram. We utilized object-oriented programming and created classes wherever possible, including generic classes that could be used by multiple files with slight parameter adjustments. For instance, View.py creates a GUI window and populates it with text passed to the class. The project primarily used three Python libraries: PyQt6, pyqtgraph, and Matplotlib (the latter two specifically for visualization). PyQt6 was employed for creating all GUI windows and facilitating communication across different functionalities. Qt Designer was used to design windows.

### About PyQt6
[PyQt6 Information](https://pypi.org/project/PyQt6/)
PyQt6 is a set of Python bindings for Qt v6, enabling Python as an alternative application development language to C++ on supported platforms. It provides comprehensive support for various aspects of modern desktop and mobile systems.

### About Qt Designer
[Qt Designer Information](https://doc.qt.io/qt-6/qtdesigner-manual.html)
Qt Designer is a tool for designing and building graphical user interfaces (GUIs) with Qt Widgets. It allows for the composition and customization of windows or dialogs in a What-You-See-Is-What-You-Get (WYSIWYG) manner, enabling testing with different styles and resolutions.

### MySQL Database
[MySQL Downloads](https://www.mysql.com/downloads/)
The database comprises 11 tables containing information about tenants, leasing managers, help providers, leases, insurance, and bills. Data types used include varchar, bigint, int, enum, and date. Foreign key integrity constraints are maintained in the database.

### Visualization
The project three visualization graphs to determine the number of help providers in each category, the gender distribution of tenants, and the number of service requests by tenants in specific categories. These visualizations help users understand the database and its associated entities. SQL queries used for these visualizations include group by clauses, count(), and joins.

### Main File
- **Main.py**: The primary file for running the application.

### Setup
1. Install Python3 on your system (tested with v3.11.0). [Python Downloads](https://www.python.org/downloads/)
2. Confirm that "python3" works on the command line to verify that the Python path is set.
3. Install the following libraries on your system: PyQt6, pyqtgraph, matplotlib.
   - Commands to run:
     - `pip3 install PyQt6`
     - `pip3 install pyqtgraph`
     - `pip3 install matplotlib`

### Command-line Instructions
- **Prerequisites**
  - Change the directory to the path where the Main.py file exists.
- **Run the following command on the terminal**:
   - `python3 Main.py` (For the main program)
   - `python3 visualization.py` 

### Specific Examples
- For user type Tenant, use credentials for users with user_id starting with 'T'.
- For user type Leasing Manager, use credentials for users with user_id starting with 'LM'.
- For user type Building Manager, use credentials for users with user_id starting with 'BM'.
- For user type Help Provider, use credentials for users with user_id starting with 'HP'.


## 3. Commands Used <a name="commands-used"></a>
1. `INSERT INTO serviceandhelper(service_id, helpprovider_id) VALUES(%s, %s)`
2. `SELECT * FROM user WHERE user_id LIKE 'T%'`
3. `SELECT * FROM user WHERE user_id LIKE 'LM%'`
4. `SELECT * FROM user WHERE user_id LIKE 'HP%'`
5. `SELECT * FROM service WHERE service_status='incomplete'`
6. `SELECT * FROM helpprovider`
7. `SELECT * FROM tenantcarddetails WHERE tenant_id=%s`
8. `SELECT name AS tenant_name, appartment_number, date_request, problem, service_description, service_status FROM service INNER JOIN serviceandhelper ON service.service_id=serviceandhelper.service_id INNER JOIN user ON user.user_id=service.tenant_id WHERE helpprovider_id=%s`
9. `SELECT name AS tenant_name, appartment_number, date_request, problem, service_description, service_status, service.service_id FROM service INNER JOIN serviceandhelper ON service.service_id=serviceandhelper.service_id INNER JOIN user ON user.user_id=service.tenant_id WHERE helpprovider_id=%s AND service_status='incomplete'`
10. `INSERT INTO tenantcarddetails(tenant_id, card_number, exp_date, security_code) VALUES(%s,%s,%s,%s)`
11. `DELIMITER $$ CREATE PROCEDURE generatebill(in lmanager_id varchar(6), in tenant_id varchar(6), in due_date varchar(255)) BEGIN insert into rentbill(lmanager_id, tenant_id, due_date, status) values(lmanager_id, tenant_id, due_date,'not paid'); end $$ DELIMITER ;`
12. `SELECT name, appartment_number, insurance_provider, tenure, insurance.start_date FROM user INNER JOIN tenant ON user.user_id=tenant_id INNER JOIN lease ON tenant.tenant_id=lease.tenant_id INNER JOIN insurance ON insurance.tenant_id=tenant.tenant_id WHERE user_id=%s`
13. `INSERT INTO user(user_id, name, gender, usercred,userpassword, date_of_birth, phone_number, nationality) values(%s, %s, %s, %s, %s, %s, %s, %s)`
14. `INSERT INTO tenant(tenant_id) values(%s)`
15. `SELECT * FROM rentbill WHERE tenant_id =%s ORDER BY due_date DESC LIMIT 1`
16. `UPDATE rentbill SET status='paid' WHERE bill_id=%s and status='not paid'`
17. `INSERT INTO service(tenant_id, date_request, problem, service_description, service_status, appartment_number) values(%s, %s, %s, %s, %s, %s)`
18. `SELECT name, gender, date_of_birth, phone_number, nationality, rent_amount, appartment_number FROM user INNER JOIN tenant ON user.user_id=tenant_id INNER JOIN lease ON tenant.tenant_id=lease.tenant_id WHERE user_id=%s`
19. `SELECT name, gender, date_of_birth, phone_number, nationality FROM user WHERE user_id=%s`
20. `SELECT role, count(*) FROM user INNER JOIN helpprovider ON user.user_id=helpprovider.helpprovider_id GROUP BY role`
21. `SELECT gender, count(*) FROM user WHERE user_id like 'T%' GROUP BY gender`
22. `SELECT problem, count(*) FROM service INNER JOIN user ON service.tenant_id=user.user_id GROUP BY problem`
23. `DELETE FROM tenantcarddetails WHERE tenantcarddetails_id=%s`
24. `SELECT * FROM service WHERE tenant_id=%s`
