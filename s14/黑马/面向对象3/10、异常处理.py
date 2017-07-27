__author = "Hu Rongyang"
try:
    11/0
    open("xxx.txt")
    print(num)
    print("------------------1----------------------") #产生异常，try里面的代码都不执行

except (NameError,FileNotFoundError): #多个异常
    print("捕捉到异常。。。。。。。。。")
except Exception as ret: #如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到")
    print(ret)

else: #没有异常才会执行的功能
    print("没有异常才会执行的功能")


finally:#不管有没有异常都会执行
            #比如程序在读取文件，人为ctrl+c停止程序引发异常（文件还没读完），需要关闭文件；
            #程序正常读完了也要关闭文件，finally就能用上了；
    print("--------------finally----------------------")

print("---------------------2------------------------")#异常处理后继续执行

'''=====================Python3中：Exception表示捕获所有异常============================'''