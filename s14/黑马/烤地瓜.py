__author = "Hu Rongyang"
class SweetPotato:
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []
    def __str__(self):
        return "地瓜 状态:%s(%d),添加的作料有：%s"%(self.cookedString,self.cookedLevel,str(self.condiments))
    def cook(self,cooked_time):
        self.cookedLevel += cooked_time
        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookedString = "半生不熟的"
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookedString = "熟了"
        elif cooked_time>8:
            self.cookedString = "烤糊了"

    def addCondiments(self,item):
        self.condiments.append(item)

#创建一个地瓜对象
di_gua = SweetPotato()
print(di_gua)

#开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("番茄酱")
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("孜然")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
