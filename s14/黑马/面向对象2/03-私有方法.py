__author = "Hu Rongyang"
class Dog:
    def __init__(self):
        self.__age = 0#定义了一个私有的属性，属性的名字是__age，现实开发中通过定义set_age方法设置，get_age方法获取

    #私有方法
    def __send_msg(self):#现实开发中，带两个下划线的私有方法比较重要，表示外部不能直接调用它，验证条件通过后才能通过自己的其他方法调用它
        print("--------------正在发送短信------------------")

    #公有方法
    def send_msg(self,new_money):
        if new_money>10000:
            self.__send_msg()
        else:
            print("余额不足，请先充值 再发送短信")

dog = Dog()
dog.send_msg(100)