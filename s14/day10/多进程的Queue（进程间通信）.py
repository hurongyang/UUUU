__author = "Hu Rongyang"
# from multiprocessing import Process,Queue
import multiprocessing

def run(qq):#子进程参数用来接收Queue
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=run, args=(q,))#把Queue通过参数传递给子进程
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

'''
多进程的Queue,其实是父进程把自己的Queue克隆一份给子进程，这时存在2个Queue,然后子进程往Queue放数据，
通过pickle序列化到一个中间方，中间方再反序列化到父进程Queue，父进程就可以取Queue的数据了，实现进程间数据传递
'''