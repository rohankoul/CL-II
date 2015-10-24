
# client side program to transfer a text file to server
import socket               # Import socket module
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)         
print "THIS IS CLIENT .."
port = 1234             # Reserve a port for your service.
s.connect(('192.168.1.20', port))
print "Connected....."
me = raw_input('ENTER STRING  : ')
s.sendall(me)
s.close()                    # Close the socket when done
