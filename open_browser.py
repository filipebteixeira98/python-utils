import webbrowser
from tkinter import *

root = Tk()

root.title('Open Browser')
root.geometry('300x200')


def launch():
    webbrowser.get('firefox').open('www.google.com')


launch_button = Button(root, text='Launch', command=launch).pack(pady=20)

root.mainloop()