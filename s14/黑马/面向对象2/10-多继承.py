class Base(object):#object是所有类的父类
    def test(self):
        print("----Base")

class A(Base):
    def test1(self):
        print("-----test1")

class B(Base):
    def test2(self):
        print("-----test2")

class C(A,B):
    pass


c = C()
c.test1()
c.test2()
c.test()
