__author = "Hu Rongyang"
#单线程下的并行运算，可以算是最简单的协程（线程下是协程）
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子，分两半!")
        c.send(i)
        c2.send(i)

producer("alex")