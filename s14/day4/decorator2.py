__author = "Hu Rongyang"
#把一个函数名当做实参传给另外一个函数
'''
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):   #func=bar，bar就是门牌号
    print(func)    #print(bar)，就是打印门牌号
    start_time=time.time()
    func()         #等于就是运行bar()  run bar()
    stop_time=time.time()
    print("the func run time is %s"%(stop_time-start_time))#打印bar()的运行时间，而不是test1的时间
test1(bar)
'''

#返回值中包含函数名
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test2(func):
    print(func)
    return func

#print(test2(bar))
bar=test2(bar)
bar()   #等于运行bar这个函数