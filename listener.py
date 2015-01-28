"""
Simple UDP listener

Usage:
  listener.py
  listener.py [<port>]
  listener.py (-h | --help)

Options:
  -h --help     Show this screen.
"""

import socket
from datetime import datetime
from docopt import docopt

host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.

if __name__ == '__main__':
    arguments = docopt(__doc__, options_first=True)
    if arguments['<port>']:
        port = int(arguments['<port>'])

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))        # Bind to the port
    print "The server is binded to", port
    while True:
        message, addr = s.recvfrom(1024)
        print "receive %s from %s" % (message, addr)
        s.sendto("I have got your message at %s" % str(datetime.now()), addr)
