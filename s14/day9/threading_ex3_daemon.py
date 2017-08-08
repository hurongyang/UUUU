__author__ = "Alex Li"

import threading
import time

def run(n):
    print("task start",n)
    time.sleep(4)
    print("task done",n,threading.current_thread())

start_time = time.time()
t_objs = []#存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)#守护线程：就是主线程的仆人，主人执行完了，子线程都会结束，不会等待子线程
    t.start()
    t_objs.append(t)#为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

# for t in t_objs:#循环线程实例列表，等待所有线程执行完毕
#     t.join()

time.sleep(2)#主线程的sleep,主线程睡2秒，子线程都是守护线程且睡4秒，所以主线程结束了子线程虽然没执行完都会结束
#time.sleep(5)#主线程睡5秒，大于子线程的4秒，所以主线程结束的时候子线程都会执行完

print("-----------------all threads has finished.....",threading.current_thread(),threading.active_count())
print("运行的时间是：",time.time()-start_time)

# run("t1")
# run("t2")