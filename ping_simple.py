# coding: utf-8
#!/usr/bin/python
import os

host = input('Enter IP to be verified: ')

os.system('ping -c 6 {}'.format(host))