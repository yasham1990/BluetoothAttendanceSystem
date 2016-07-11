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
                q = "Select STATUS FROM " + tablename + " WHERE NAME = ?" + " AND SID = ?" + " AND PASSWORD = ?" 
                print q
                cur = con.cursor() 
                cur.execute(q,(ljson['ename'], ljson['eid'], ljson['epass']))
		 
                
		data = cur.fetchone()
                
		
                
		if data == None:
		   return "3" ##Datarecord not present
	        r = data[0]
                res = int(r)
                print res
                if res == 0: 
                   query = "UPDATE " + tablename +" SET STATUS = 1, MADDRESS = ?" + " WHERE SID = ?" 
                   cur.execute(query,(ljson['bid'], ljson['eid']))
                   con.commit()
                   return "1" ##registered
                else:
                   return "2" ##already registered
                
       

    		
        
    
	except lite.Error, e:
    		
    		return e.args[0]
    		
    
	finally:
    
    		if con:
        		con.close()
