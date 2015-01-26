import socket               # Import socket module

host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.

if __name__ == '__main__':
    s = socket.socket()         # Create a socket object
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    print "Wating for client..."
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        f = open('send.pdf')
        c.sendall(f.read())
        print "File sent"
        c.close()                # Close the connection
