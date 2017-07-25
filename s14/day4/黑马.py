__author = "Hu Rongyang"
class Cat:
    '''定义一个Cat类'''

    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return "%s的年龄是：%d"%(self.name,self.age)
    #方法
    def eat(self):
        print("%s在吃鱼。。。"%self.name)

    def drink(self):
        print("%s正在喝可乐。。。"%self.name)

    def introduce(self):
        print("%s的年龄是：%d"%(self.name,self.age))

#创建一个对象
tom = Cat('汤姆',40)

lanmao = Cat('蓝猫',10)

print(tom)
print(lanmao)




























































































































































'''
#人 类
class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name + "剩余血量为："+str(self.xue)

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shasahngli):
        self.xue -= shasahngli

#弹夹类
class Danjia:
    def __init__(self,ronglaing):
        self.ronglaing = ronglaing
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为："+str(len(self.rongnaList))

    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.ronglaing:
            self.rongnaList.append(zidan)
'''
