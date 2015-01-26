"""
Simple TCP Server

Usage:
  server.py <filename> [<host>] [<port>]
  server.py (-h | --help)

Options:
  -h --help     Show this screen.
"""

import socket               # Import socket module
from docopt import docopt

host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.
filename = 'send.pdf'

if __name__ == '__main__':
    arguments = docopt(__doc__, options_first=True)
    filename = arguments['<filename>']
    if arguments['<host>']:
        host = arguments['<host>']
    if arguments['<port>']:
        port = arguments['<port>']

    s = socket.socket()         # Create a socket object
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    print "Wating for client..."

    while True:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr

        c.sendall(filename)
        f = open(filename)
        c.sendall(f.read())
        print "File sent"
        
        c.close()                # Close the connection
