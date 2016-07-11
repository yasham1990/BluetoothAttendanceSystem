import time
import datetime

d = datetime.date.today()


def dobject(text):
     
     
     ss =text.split(":")
     t = datetime.time(int(ss[0]), int(ss[1]))
     stt = datetime.datetime.combine(d, t)
     print stt
     return stt

def checktimestamp(stime, etime):
     

     starttime = dobject(stime)
     endtime = dobject(etime) 
     dt = datetime.datetime.now()
     t = datetime.time(int(dt.hour), int(dt.minute), int(dt.second))
     currenttime = datetime.datetime.combine(d, t)
     #currenttime = dobject("14:00")
     
     print currenttime
     

     if currenttime > starttime and currenttime < endtime:
          print "hello"
          return str(currenttime)
     else:
          return "-1"



#time.sleep(20)

#n = datetime.strptime(st, "%Y-%m-%d %H:%M:%S.%f")
#print n

     print "------"

     


