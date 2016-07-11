# Team-Mavericks
CMPE-273 Final Project
eAttendane System

By:
Chandra Shekhar  
Piyush Katiyar  
Pratheeksha Devegowda  
Yasham Singhal


===============================================
The main feature of the project is that it only uses Bluetooth as the medium of communication. Right from receiving the data from the Android App and storing the received data into the database, everything is achieved via Bluetooth only.  


The project includes Raspberry Pi as server, SqliteDB on server for records storage. Android application is used by students to register, login, checkin to the classes registered. The attendance system can be viewed locally on the server and also on cloud. The DB on server and EC2 cloud is synchronized every 1 min.

1.Rfcomm Server- python scripts on server. registerrfcommserver is to start registration server,loginrfcommserver forlogin and checkinrfcommserver for checkin. The rfcommservers are started on powering the raspberry pi. Manually it can be done by starting newscript.sh  
2.eAttendance - Django and html files for UI. The UI server is started as  
$sudo python manager.py runserver  
3.eAttendanceApp - Android application to connect device to server.

