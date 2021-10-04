import ctypes

attr_hide = 0x02
hidden_file = ctypes.windll.kernel32.SetFileAttributesW('hide.txt', attr_hide)

if hidden_file:
    print('File was hidden')
else:
    print('It was not possible to hide such archive')