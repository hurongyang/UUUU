__author = "Hu Rongyang"
import threading
import time

event =threading.Event()

def lighter():
    count = 0
    event.set()#先设置绿灯
    while True:
        if count > 5 and count < 10:#改成红灯
            event.clear()#把标志位清空
            print("\033[41;1m red light is on......\033[0m")
        elif count >10:
            event.set()#变绿灯
            count = 0
        else:
            print("\033[46;1m green light is on......\033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():#有设置标志位，代表绿灯
            print("[%s] running...."% name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..."% name)
            event.wait()
            print("[%s] green light is on,start going......"% name)


light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()