__author__ = "Alex Li"

import threading
import time

num = 0
lock = threading.Lock()#锁

def run(n):
    lock.acquire()#加锁
    global num
    num += 1
    time.sleep(0.1)
    lock.release()#释放锁

t_objs = []#存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_objs.append(t)#为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs:#循环线程实例列表，等待所有线程执行完毕
    t.join()#join是等待所有的子线程执行完毕

print("-----------------all threads has finished.....",threading.current_thread(),threading.active_count())

print("number:",num)