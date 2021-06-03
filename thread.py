# coding: utf-8
#!/usr/bin/python
from threading import Thread
import time
import uuid


def concurrency(pace, thread_id):
    arrival = 0

    while arrival <= 100:
        arrival += pace
        time.sleep(0.5)
        print('thread_id: {} arrival: {}'.format(thread_id, arrival))


first_thread = Thread(target=concurrency, args=[1, uuid.uuid4().hex])
second_thread = Thread(target=concurrency, args=[2, uuid.uuid4().hex])

first_thread.start()
second_thread.start()