# coding: utf-8
#!/usr/bin/python
import itertools

word = input('Enter string to be permuted: ')
result = itertools.permutations(word, len(word))

for character in result:
    print(''.join(character))
