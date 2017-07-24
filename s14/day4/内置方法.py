__author = "Hu Rongyang"
abs()        #取绝对值

all()        #所有都为真才返回真      all([0,-5,3])
any()        #有一个为真返回真        all([0,-5,3])

bin()        #十进制转二进制
bool()       #布尔

bytearray()
bytes()

callable()   #判断是否可以调用        print(callable([1,2,3]))

chr()        #返回对应数字ascill码对应的字符      chr(98)
ord()        #返回ascill码字符对应的数字          ord(b)

delattr()    #
dict()       #字典
dir()        #查看所有可用的方法       print(dir([]))
divmod()     #相除返回（商，余数）         divmod(5,3)
enumerate()  #枚举

eval()       #把一个字符串变成一个字典
exec()

filter()     #过滤
    # res = filter(lambda n :n > 5,range(10))
    # for i in res:
    #     print(i)
map()       #一个个处理
    # res = map(lambda n :n * 5,range(10))
    # for i in res:
    #     print(i)
# 。。。。。。。。。。。。。。。。。。。。。。。。