__author = "Hu Rongyang"
import threading
import queue
import time


q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:
            q.put("骨头-%s" %count )
            print("[%s] 开始制造骨头 [%s]"% (name,count))
            count += 1
            time.sleep(0.5)

def Consumer(name):
    while True:
        print("[%s] 取到[%s] 并且吃了它。。。。。" %(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("Alex",))
c = threading.Thread(target=Consumer,args=("陈荣华",))
c1 = threading.Thread(target=Consumer,args=("王森",))

p.start()
c.start()
c1.start()