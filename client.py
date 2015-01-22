import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
f = open('receive.pdf', 'w')
temp = s.recv(1024)
while temp:
	f.write(temp)
	temp = s.recv(1024)
f.close()
s.close()                     # Close the socket when done
