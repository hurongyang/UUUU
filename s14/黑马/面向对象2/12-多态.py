class Dog:
    def print_self(self):
        print("大家好,我是xxxx,希望以后大家多多关照....")

class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody, 我是你们的老大,我是xxxx")


def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()

#多态：不确定调用父类还是子类，只有调用的时候才确定
introduce(dog1)#dog1赋值给temp,则temp指向Dog()
introduce(dog2)#dog2赋值给temp,则temp指向Xiaotq(Dog)
