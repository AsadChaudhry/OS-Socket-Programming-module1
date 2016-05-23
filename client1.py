
import socket               # Import socket module
import thread
s = socket.socket()
host = socket.gethostname()
port = 5581   # Reserve a port for your service.
s.connect((host, port))
print s.recv(1024)
def rc():
    while True:
        data=s.recv(1024)
        print 'user2:',data
thread.start_new_thread(rc,())
while True:
    s.send(raw_input())
s.close                     # Close the socket when done
