__author = "Hu Rongyang"
from multiprocessing import Process, Manager
import os
def f(d, L):
    d[os.getpid()] = os.getpid()
    L.append(os.getpid())
    print(L)

if __name__ == '__main__':

    manager = Manager()
    d = manager.dict()#生成可在多个进程之间传递和共享的字典
    L = manager.list(range(5))#生成可在多个进程之间传递和共享的列表
    p_list = []
    for i in range(10):
        p = Process(target=f, args=(d, L))
        p.start()
        p_list.append(p)
    for res in p_list:
        res.join()

    print(d)
    print(L)