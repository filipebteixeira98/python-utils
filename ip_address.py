# coding: utf-8
#!/usr/bin/python
import ipaddress

ip = '192.168.0.1'
subnet_mask = '192.168.0.1/24'

addr = ipaddress.ip_address(ip)

print('localhost: ', addr)

network = ipaddress.ip_network(subnet_mask, strict=False)

for interface in network:
    print('available interface: ', interface)