#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def update(tablename, ljson):
	con = None
	
	

	try:
    		con = lite.connect('/home/cmpe273/cmpe273/CMPE273.db')
    
    		cur = con.cursor()    
    		cur.execute('SELECT SQLITE_VERSION()')
    
	    	data = cur.fetchone()
    
    		print "SQLite version: %s" % data
                q = "Select COUNT(*) FROM " + tablename + " WHERE SID = ?" + " AND MADDRESS = ?" + " AND PASSWORD = ?" 
                print q
                cur = con.cursor() 
                cur.execute(q,(int(ljson['lid']), ljson['bid'], ljson['lpass']))
		 
                
		data = cur.fetchone()
                
		
                
		if data == None:
		   return "3" ##data not found
	        r = data[0]
                res = int(r)
                print res
                if res == 1: 
                   return "1" ##success
                else:
                   return "2" ##login failure
                
       

    		
        
    
	except lite.Error, e:
    		
    		return e.args[0]
    		
    
	finally:
    
    		if con:
        		con.close()
