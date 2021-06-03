# coding: utf-8
#!/usr/bin/python
import hashlib

file = 'hashed.txt'
another_file = 'another_hashed.txt'

hashed_file = hashlib.new('ripemd160')

hashed_file.update(open(file, 'rb').read())

another_hashed_file = hashlib.new('ripemd160')

another_hashed_file.update(open(another_file, 'rb').read())

if hashed_file.digest() != another_hashed_file.digest():
    print('both files have different hashes\n first: {}\n second: {}'.format(
        hashed_file.hexdigest(), another_hashed_file.hexdigest()))
else:
    print('both files have compatible hashes %s' % (hashed_file.hexdigest()))