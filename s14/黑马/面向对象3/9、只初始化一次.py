__author = "Hu Rongyang"
class Dog(object):

    __instance = None

    def __new__(cls,name):                      #
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return 上一次创建的对象的引用
            return cls.__instance

    def __init__(self,name):
        self.name = name

a = Dog("旺财")#因为先调__new__方法,而"旺财"又不能传给cls，会报错，所以得给__new__方法加一个name参数
print(id(a))
print(a.name)

b = Dog("哮天犬")
print(id(b))
print(b.name)
'''
打印结果：
    1267913840064
    旺财
    1267913840064
    哮天犬             ========================》      name属性被修改为了哮天犬
'''