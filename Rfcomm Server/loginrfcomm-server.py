import thread
import ast
import time

from dblogin import update
from bluetooth import *

def clientsocket(clientsock, clientinfo):
	print("Accepted connection from ", client_info[0])
        #time.sleep(20)
	try:
            while True:
                data = client_sock.recv(1024)
                print data
                msg_client = ast.literal_eval(data)
                print msg_client
                msg_client.update({'bid': client_info[0]})
                #print msg_client["name"]
                #formattedmsg = [ msg_client["name"],msg_client["email"], msg_client["id"] , msg_client["phone"], client_info[0] ]
		print msg_client 
		#newlist = list(msg_client.values())
                #newlist.append(client_info[0])
		#print newlist
		msg = update('REGISTER', msg_client)
                #print("received [%s]" % data);
		print msg
                client_sock.sendall(msg);
          
                break
        except IOError:
            pass
         
        print("disconnected")

        client_sock.close()

	


server_sock=BluetoothSocket( RFCOMM )
#port = server_sock.getsockname()[1]
server_sock.bind(("",PORT_ANY))
server_sock.listen(5)
#port = server_sock.getsockname[1]
port = server_sock.getsockname()[1]


uuid = "94f39d29-7d6d-437d-973b-fba39e49d4aa"
#insert('Student', ['cc', 'dd', 44, 66,  '3'])
advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
while True:                   
	print("Login server -- Waiting for connection on port ",  port)

	client_sock, client_info = server_sock.accept()
	print "server port ",  server_sock.getsockname()[1]
        thread.start_new_thread(clientsocket,(client_sock, client_info))
        '''
	print("Accepted connection from ", client_info)

	try:
	    while True:
		data = client_sock.recv(1024)
		print data
                msg_client = ast.literal_eval(data)
		print msg_client["name"]
		print("received [%s]" % data);
                client_sock.sendall("done");
          
		break
	except IOError:
	    pass
         
	print("disconnected")

	client_sock.close()
        ''' 
server_sock.close()
print("all done")

