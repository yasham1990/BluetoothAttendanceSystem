#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE Student
       ( Name TEXT    NOT NULL,
       Email  CHAR(50),
       ID INT PRIMARY KEY NOT NULL,
       Phone INT NOT NULL,     
       Bid CHAR(20));''')
print "Table created successfully";

conn.close()
