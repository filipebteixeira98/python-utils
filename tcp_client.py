# coding: utf-8
#!/usr/bin/python
import socket
import sys
from string import Template


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as err:
        print('error trying to connect with O.S SOCKET API: {}'.format(err))
        sys.exit()

    print('socket created successfully')

    host = input('host: ')
    port = input('port: ')

    try:
        s.connect((host, int(port)))
        print('TCP client connected successfully [%s:%s]' % (host, port))
        s.shutdown(2)
    except socket.error as err:
        literal = Template('error trying to reach [$h:$p] $e')
        print(literal.substitute(h=host, p=port, e=err))


if __name__ == '__main__':
    main()