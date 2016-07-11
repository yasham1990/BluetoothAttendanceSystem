               #!/usr/bin/python

import sqlite3

conn = sqlite3.connect('CMPE273.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE REGISTER
       ( NAME TEXT    NOT NULL,
       EMAIL  TEXT,
       SID INT PRIMARY KEY NOT NULL,
       PASSWORD TEXT,
       STATUS INT,     
       MADDRESS TEXT,
       UNIQUE (EMAIL, SID));''')
print "Table1 created successfully";

conn.execute('''CREATE TABLE CHECKIN
       ( SID INT    NOT NULL,
       CLASSID  TEXT,
       CHECKIN TEXT,
       CHECKOUT TEXT,
       ATTENDANCE INT);''')
print "Table2 created successfully";

conn.execute('''CREATE TABLE CLASSDESC
       ( CLASSID TEXT    NOT NULL,
       STARTTIME TEXT NOT NULL,
       ENDTIME TEXT NOT NULL,
       DAY INT NOT NULL,
       PRIMARY KEY (CLASSID));''')
print "Table3 created successfully";

conn.execute('''CREATE TABLE STUDENTCLASS
       ( SID INT    NOT NULL,
       CLASSID  TEXT NOT NULL,
       PRIMARY KEY (SID, CLASSID));''')
print "Table4 created successfully";


conn.close()
