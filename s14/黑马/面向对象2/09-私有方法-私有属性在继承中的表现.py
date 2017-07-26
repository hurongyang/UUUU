class A:
    def __init__(self):
        self.num1 = 100

        #私有属性
        self.__num2 = 200

    def test1(self):
        print("-----test1----")

    #私有方法
    def __test2(self):
        print("-----test2----")

    def test3(self):
        self.__test2()
        print(self.__num2)

class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)


b = B()
b.test1()
#b.__test2()     #私有方法并不会被继承
print(b.num1)
#print(b.__num2) #私有属性不会被继承

b.test3()        #通过class A的公有方法test3里调用自己的私有属性和私有方法是可以的
# b.test4()      #对象A的私有属性和私有方法，对像B不能继承，是不能直接调用的
