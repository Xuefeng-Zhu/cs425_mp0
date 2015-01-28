import socket               # Import socket module
from datetime import datetime

host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.

if __name__ == '__main__':
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))        # Bind to the port
    while True:
        message, addr = s.recvfrom(1024)
        print "receive %s from %s" % (message, addr)
        s.sendto("I have got your message at %s" % str(datetime.now()), addr)
