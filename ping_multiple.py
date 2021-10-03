# coding: utf-8
#!/usr/bin/python
import os
import time

with open('hosts.txt') as file:
  dump = file.read()
  dump = dump.splitlines()

  for ip in dump:
    print('Trying to reach out IP: ' + ip)
    os.system('ping -c 2 {}'.format(ip))
    time.sleep(5)