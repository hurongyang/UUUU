class Base(object):
    def test(self):
        print("----Base")

class A(Base):
    def test(self):
        print("-----A")

class B(Base):
    def test(self):
        print("-----B")

class C(B,A):
    pass
    #def test(self):
    #    print("-----C")


c = C()
c.test()#调用B的test方法

'''
1、如果A B C都有一个同名方法test，则只调自己的输出("-----C")
2、如果B C都有一个同名方法test，则C多继承的时候(B,A)     =======》A在前，调用A的test方法；B在前调用B的test方法
'''
print(C.__mro__)#决定搜索的优先顺序
'''(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.Base'>, <class 'object'>)'''