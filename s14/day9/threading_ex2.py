__author__ = "Alex Li"

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super().__init__()
        self.n =  n
        self.sleep_time = sleep_time

    def run(self):
        print("runnint task ",self.n )
        time.sleep(self.sleep_time)
        print("task done",self.n)

t1 = MyThread("t1",2)
t2 = MyThread("t2",2)

t1.start()
t2.start()
t1.join()#join是等待t1子线程执行完毕
t2.join()#join是等待t2子线程执行完毕

print("main thread....")

