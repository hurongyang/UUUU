__author = "Hu Rongyang"
class Dog(object):
    def __init__(self):
        print("----init方法-----")

    def __del__(self):
        print("----del方法-----")

    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls):#重写__new__方法            cls此时是Dog指向的那个类对象

        #print(id(cls))

        print("----new方法-----")
        return object.__new__(cls)#虽然重写了__new__方法，但是只能打印，还是得调用父类（object）的__new__方法才能创建对象


#print(id(Dog))

xtq = Dog()#相当于做三件事
'''
输出结果：
----new方法-----
----init方法-----
----del方法-----
相当于做三件事。。。
'''

'''
            1、__new__方法（只负责创建对象）来创建对象，然后找一个变量来接收__new__的返回值，这个返回值表示创建的对象的引用
            2、__init__方法（只负责初始化）
            3、__del__方法（只负责删除对象）
            4、java的构造方法：既有创建，又有初始化，所以和python不同
'''