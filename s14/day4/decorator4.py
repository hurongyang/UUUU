__author = "Hu Rongyang"
# 装饰器
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return deco

@timer  #test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')

@timer   #test2=timer(test2)
def test2(name,age):
    print('test2:',name,age)


test1()
test2('alex',22)



# test1()
# test2()