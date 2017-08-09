__author = "Hu Rongyang"
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child2'])
    print("from parent:",conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()#生成管道实例会返回两个实例对象
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    parent_conn.send("你好啊，子进程。。。。。")
    p.join()