__author = "Hu Rongyang"
#from multiprocessing import Process, Lock
import multiprocessing

#进程锁是因为屏幕是共享的，如果不加锁打印的时候有可能乱
def f(n, i):
    n.acquire()
    print('hello world', i)
    n.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()

    for num in range(10):
        multiprocessing.Process(target=f, args=(lock, num)).start()