#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from datetime import date
import timestampdate


def update(ljson):
	con = None
	
	

	try:
    		con = lite.connect('/home/cmpe273/cmpe273/CMPE273.db')
    
    		cur = con.cursor()    
    		cur.execute('SELECT SQLITE_VERSION()')
    
	    	data = cur.fetchone()
    
    		print "SQLite version: %s" % data
                ##q = "Select CLASSDESC.STARTTIME, CLASSDESC.ENDTIME, CLASSDESC.DAY FROM CLASSDESC INNER JOIN STUDENTCLASS ON CLASSDESC.CLASSID = STUDENTCLASS.CLASSID"
                #CREATE TEMP VIEW STUDVIEW AS SELECT DISTINCT CLASSID FROM STUDENTCLASS
                q = "Select CLASSDESC.STARTTIME, CLASSDESC.ENDTIME, CLASSDESC.DAY FROM CLASSDESC  WHERE CLASSDESC.CLASSID = ?" 
                print q
                cur = con.cursor() 
                cur.execute(q,(ljson['course'],))
		      
                
		data = cur.fetchone()
                
		
                
		if data == None:
		   return "DataRecord not present"
                print data
	        starttime = data[0]
                endtime = data[1]
                day = int(data[2])
                currentday = date.today()
                
                
                
                

                if day == currentday.weekday():
                    
                    rescheckin = timestampdate.checktimestamp(starttime, endtime)
                    print rescheckin
                    if rescheckin == "-1":
                         return "Attendance not marked,timeover"

                    tempdate = (rescheckin.split(' '))[0]
                    query = "Select substr(CHECKIN, 1, 10) from CHECKIN where CHECKIN.SID = ? and CHECKIN.CLASSID = ?"
                    cur.execute(query,(ljson['cid'], ljson['course'], ))
                    checkindata = cur.fetchall()
                    if not (checkindata is None):
                        for checkdate in checkindata:
                            if checkdate[0] == tempdate:
                                return "Already Checked In"

                    query = "INSERT INTO CHECKIN (SID, CLASSID, CHECKIN, ATTENDANCE) VALUES (?,?,?,?)" 
                    cur.execute(query,(ljson['cid'], ljson['course'], rescheckin, 1 ))
                    con.commit()
                    return "Attendance marked"
                else:
                    return "Invalid checkin"
             

                
                
       

    		
        
    
	except lite.Error, e:
    		
    		return e.args[0]
    		
    
	finally:
    
    		if con:
        		con.close()
