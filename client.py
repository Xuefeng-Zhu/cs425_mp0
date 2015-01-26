import socket               # Import socket module

host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.

if __name__ == '__main__':
    s = socket.socket()         # Create a socket object
    s.connect((host, port))
    print "Connect to ", (host, port)
    with open('receive.pdf', 'w') as f:
        temp = s.recv(1024)
        while temp:
            f.write(temp)
            temp = s.recv(1024)
    print "Receive file"
    s.close()                     # Close the socket when done
