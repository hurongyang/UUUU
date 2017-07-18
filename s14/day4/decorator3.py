__author = "Hu Rongyang"
# 嵌套函数
def foo():
    print('in the foo')
    def bar():
        print('in the bar')

    bar()
foo()

