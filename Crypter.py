def change_files(filename, cryptoFn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)

        while raw_value:
            cipher_value = cryptoFn(raw_value)

            if len(raw_value) is not len(cipher_value):
                raise ValueError('Values do not match! {} != {}'.format(
                    len(cipher_value), len(raw_value)))

            _file.seek(-len(raw_value), 1)
            _file.write(cipher_value)

            raw_value = _file.read(block_size)