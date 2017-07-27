__author = "Hu Rongyang"
'''
单例对象：不管创建多少个对象，他们都是指向同一个对象，对象只有一个
          例如：windows电脑窗口就是一个单例对象，就是说不管你打开了多少个窗口，都是指向的同一个对象
'''
class Dog(object):

    __instance = None

    def __new__(cls):                      #重写__new__方法
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return 上一次创建的对象的引用
            return cls.__instance

a = Dog()
print(id(a))
b = Dog()
print(id(b))
'''
打印结果：
        2249048561480
        2249048561480
结论：
        a和b指向的是同一个对象
'''