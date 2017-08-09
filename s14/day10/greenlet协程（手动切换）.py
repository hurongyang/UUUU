from greenlet import greenlet

'''greenlet属于手动切换（手动挡），gevent是把greenlet封装实现自动切换（自动挡）'''
def test1():
    print(12)        #==>2
    gr2.switch()     #==>3
    print(34)        #==>6
    gr2.switch()     #==>7

def test2():
    print(56)        #==>4
    gr1.switch()     #==>5
    print(78)        #==>8

gr1 = greenlet(test1)#启动一个协程
gr2 = greenlet(test2)#启动一个协程
gr1.switch()         #==>1