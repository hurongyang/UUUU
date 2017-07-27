class Dog:
    
    def __del__(self):
        print("-----英雄over------")

dog1 = Dog()
dog2 = dog1

del dog1#不会调用 __del__方法,因为这个对象 还有其他的变量指向它,即 引用计算不是0
del dog2#此时会调用__del__方法,因为没有变量指向它了
print("====================")

#如果在程序结束时,有些对象还存在,那么python解释器会自动调用它们的__del__方法来完成清理工作

'''
dog1 = Dog()
dog2 = dog1
del dog1
#dog1 dog2两个都是指向Dog对象的引用，只删除了dog1引用，dog2引用还在，即对象Dog不会删除。只有当下面的print执行完后，程序即将结束(删除Dog)之前才执行__del__方法
print("================================")
'''

'''
dog1 = Dog()
dog2 = dog1
del dog1
del dog2
#dog1 dog2两个指向Dog对象的引用都删除了，代表删除对象，__del__会在删除对象Dog之前执行，即优先于下面的print输出
print("================================")
'''