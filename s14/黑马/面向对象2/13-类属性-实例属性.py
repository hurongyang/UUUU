class Tool(object):#Python中类也是一个对象,叫类对象（包含类属性，类方法）
    def __init__(self, new_name):
        self.name = new_name


num = 0
tool1 = Tool("铁锹")#实例化的对象称为实例对象（包含实例属性，实例方法）
num+=1
print(num)
tool2 = Tool("工兵铲")
num+=1
print(num)
tool3 = Tool("水桶")
num+=1
print(num)
