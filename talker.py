"""
Simple UDP talker

Usage:
  talker.py
  talker.py [<host>] [<port>]
  talker.py (-h | --help)

Options:
  -h --help     Show this screen.
"""

import socket
from docopt import docopt

host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.

if __name__ == '__main__':
    arguments = docopt(__doc__, options_first=True)
    if arguments['<host>']:
        host = arguments['<host>']
    if arguments['<port>']:
        port = int(arguments['<port>'])

    # Create a socket object
    addr = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = raw_input("What are you going to say: ")
        s.sendto(message, addr)
        message = s.recvfrom(1024)[0]
        print "reply: %s" % message
