# coding: utf-8
#!/usr/bin/python
import hashlib

key = input('enter your key to generate hash: ')

kind = int(
    input('''
choose type of algorithm

1) MD5
2) SHA1
3) SHA256
4) SHA512

> '''))

if kind == 1:
    hashed = hashlib.md5(key.encode('utf-8'))
    print('MD5: ', hashed.hexdigest())
elif kind == 2:
    hashed = hashlib.sha1(key.encode('utf-8'))
    print('SHA1: ', hashed.hexdigest())
elif kind == 3:
    hashed = hashlib.sha256(key.encode('utf-8'))
    print('SHA256: ', hashed.hexdigest())
else:
    hashed = hashlib.sha512(key.encode('utf-8'))
    print('SHA512: ', hashed.hexdigest())