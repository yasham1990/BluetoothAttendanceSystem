#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db')
    
    cur = con.cursor()    
    #cur.execute('SELECT SQLITE_VERSION()')
    print " ----- all rows---------"

    cur.execute("SELECT * FROM Student")
    data = cur.fetchall()
    print data
    print "-------------------"

    
    print "Records printed successfully";
        
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
