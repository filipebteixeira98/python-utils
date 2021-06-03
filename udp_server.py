# coding: utf-8
#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('socket created successfully')

host = 'localhost'
port = 5432
message = 'flag [SYN/ACK] packet'

s.bind((host, port))

while True:
    data, address = s.recvfrom(4096)

    if data:
        print('sending message to client')
        s.sendto(message.encode(), address)