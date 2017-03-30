__author = "Hu Rongyang"
def test(x,y=2):   #默认参数，只能放在最后
    print(x)
    print(y)

test(1)
test(1,3)     #调用函数的时候，默认参数非必须传递
test(1,y=3)  #调用函数的时候，默认参数非必须传递
#默认参数用途：