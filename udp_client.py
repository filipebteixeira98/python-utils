# coding: utf-8
#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('socket created successfully')

host = 'localhost'
port = 5433
message = 'flag [SYN] packet'

try:
    print('udp client: send {}'.format(message))
    s.sendto(message.encode(), (host, 5432))
    print('trying to establish three way handshake')

    data, address = s.recvfrom(4096)
    data = data.decode()

    print('udp server: returned %s' % (data))
finally:
    print('udp client has ended up connection')
    s.close()