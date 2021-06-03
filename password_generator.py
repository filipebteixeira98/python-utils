# coding: utf-8
#!/usr/bin/python
import random
import string

size = int(input('bytes [offset] of password: '))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))