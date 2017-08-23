import multiprocessing
import time,threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_run,)#每个进程里面启动一个线程
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('Alex-[%s]'%i,))
        p.start()

    # p.join()

