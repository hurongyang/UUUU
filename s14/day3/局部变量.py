__author = "Hu Rongyang"

school = "oldboy edu"#全局变量,在函数里是可以访问的

def change_name(name):
    school = "Mage Linux" #再定义一个school变量，函数里访问的就是函数里的school,而是不全局定义的school
    print("before change:",name,school)
    name = "ALex Li" #局部变量只在函数里生效，这个函数就是这个变量的作用域
    age=23
    print("after change:",name)

name = 'alex'
change_name(name)
print(name)
#print('age',age)这个是不行的
print(school)#还是oldboy


print("===================================")
#如果非要在函数里改全局变量，在声明变量的时候加global，实际中不应该在函数中定义全局变量
def change_name1():
    global school
    school = "Mage Linux"
    print(school)
change_name1()
print(school)
