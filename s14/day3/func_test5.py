__author = "Hu Rongyang"
def test(x,y):  #x,y就是形参
    print(x)
    print(y)

test(1,2)       #1,2就是实参,位置参数调用要与形参一一对应
test(x=2,y=1)   #关键字调用，与形参顺序无关
#关键参数是不能写在位置参数前面的