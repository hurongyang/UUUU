__author = "Hu Rongyang"

'''def change_name():
    global name
    name = 'alex'
change_name()
print(name)#打印结果是alex,在函数体里定义全局变量也是可以的,但是不应该这么干
'''


school = "oldboy edu"
names = ["alex","jack","rain"]

def change_name():
    print('===========>',names)
    names[0] = "金角大王"#这个是可以修改成功的,像列表，字典，集合，类里面的元素是可以改的
    print('函数里面：',names)#结果是金角大王
change_name()
print('函数外面：',names)#结果是金角大王，列表内元素是可以改的，因为列表内存对象没变