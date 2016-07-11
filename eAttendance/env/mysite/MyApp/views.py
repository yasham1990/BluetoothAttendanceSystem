from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from django.db import models
from MyApp.models import Classdesc, Checkin, Studentclass
from MyApp.DatabaseManagement import DatabaseManager
import sys
import sqlite3 as lite
from _sqlite3 import Cursor
def index(request):
    con = None
    #p= None
    classname= None
    classdate= None
    attendance= None
    data = None
    if request.method == 'POST':
        classname = request.POST['subject']
        attendance = request.POST['attendance']
        
        temp = str(request.POST['classdate'])
        print temp
        classdate = request.POST['classdate'] + '%' 
        dbmgr = DatabaseManager("/home/cmpe273/cmpe273/CMPE273.db")
        #if attendance == 'all':
        query = "select studentclass.sid,register.name,studentclass.classid,'' as TIME,'%s' as DATE,'0' as ATTENDANCE  from studentclass,register  where not studentclass.sid in ( select studentclass.sid from checkin, studentclass where checkin.sid= studentclass.sid and checkin.classid=studentclass.classid and studentclass.classid='%s' and checkin like ?) and classid='%s' and studentclass.sid= register.sid union select checkin.sid, NAME, checkin.classid,substr( CHECKIN, 12) AS Time,substr( CHECKIN, 1, 10) AS Date, ATTENDANCE  from checkin,studentclass,register where register.sid=studentclass.sID  and checkin.CHECKIN like  ? and checkin.CLASSID='%s' and checkin.sid=studentclass.sID and checkin.CLASSID=studentclass.classid" % (temp, classname, classname, classname)
        #query = "select checkin.sid, NAME, checkin.classid,substr( CHECKIN, 12) AS Time,substr( CHECKIN, 1, 10) AS Date, ATTENDANCE  from checkin,studentclass,register where register.sid=studentclass.sID  and checkin.CHECKIN like  ? and checkin.CLASSID='%s' and checkin.sid=studentclass.sID and checkin.CLASSID=studentclass.classid" % classname
        rs = dbmgr.query(query,(classdate,classdate,),)
        data = rs.fetchall()
        for d in data:
            print d
        
        #=======================================================================
        # try:
        #     con = lite.connect('/Users/PKatiyar/Desktop/CMPE-273/DB/CMPE273.db')
        #     cur = con.cursor
        #     #cur.execute('SELECT SQLITE_VERSION')
        #     query = "select checkin.sid, checkin.classid, CHECKIN, CHECKOUT, ATTENDANCE from checkin, studentclass where checkin.CHECKIN like ? and checkin.CLASSID=? and checkin.sid=studentclass.sID and checkin.CLASSID=studentclass.classid"
        #     data = con.execute(query, (classdate, classname,));
        # except lite.Error, e:
        #     print "Error %s:" % e.args[0]
        #     sys.exit(1)
        # finally:
        #     if con:
        #         con.close()
        #=======================================================================

    classdata = Classdesc.objects.only("classid")
    t = loader.get_template('index.html')
    c = RequestContext(request, {'classdata': classdata, 'attendance': attendance, 'a':classname, 'b': classdate, 'studentdata': data}, )
    return HttpResponse(t.render(c))


#===============================================================================
# def insert(request):
#     # If this is a post request we insert the person
#     if request.method == 'POST':
#         p = User(
#             sname=request.POST['sname'],
#             sid=request.POST['sid'],
#             email=request.POST['email'],
#             subject=request.POST['subject']
#         )
#         p.save()
# 
#     t = loader.get_template('insert.html')
#     c = RequestContext(request)
#     return HttpResponse(t.render(c))
#===============================================================================
