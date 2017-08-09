__author = "Hu Rongyang"
from  multiprocessing import Process,Pool
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i+100

def Bar(arg):
    print('-->exec done:',arg,os.getpid())

print(__name__)
if __name__ == '__main__':
    pool = Pool(processes=3)
    print("主进程PID：",os.getpid())
    for i in range(15):
        #pool.apply(func=Foo, args=(i,))            #串行
        #pool.apply_async(func=Foo, args=(i,))      #并行
        pool.apply_async(func=Foo, args=(i,),callback=Bar)#callback=回调,回调就是Foo执行完了就执行Bar
        '''
        回调的场景：比如我起100个进程做数据库备份，备份完之后立马写一条日志到数据库，如果不用回调，就得起100个线程连接100
        次数据库，造成很大开销；如果用回调的话，因为回调是回调主线程，所以只需要连接一次就可以了
        '''
    print('end')
    pool.close()
    pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。