__author = "Hu Rongyang"
def test(x,y,z=2):
    print(x)
    print(y)
    print(z)
test(1,2,z=3)
print("=========================================")

#*args：接收N个位置参数，转换成元组的方式
def test2(*args):
    print(args)
test2(1,2,3,4,5,6,7)
test2(*[1,2,3,5,5,5,6,7,8,])
print("=========================================")

def test3(x,*args):
    print(x)
    print(args)
test3(1,2,3,4,5,6,7,8,9)
print("=========================================")

#**kwargs:接收N个关键字参数，转换成字典的方式
def test4(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])
test4(name="alex",age=8,sex="F")
#test4(**{'name':'alex','age':8,'sex':'F'})
print("=========================================")

def test5(name,**kwargs):
    print(name)
    print(kwargs)
test5('alex',age=18,sex='m')
print("=========================================")

def test6(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)
test6('alex',5,sex='m',salary=2000)
test6('alex',age=5,sex='m',salary=2000)
test6('alex',sex='m',salary=2000,age=5)
print("=========================================")

def test7(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
test7('alex',age=34,ser='m',hobby='tesla')