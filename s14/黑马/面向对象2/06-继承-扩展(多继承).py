__author = "Hu Rongyang"
class Animal:
    def eat(self):
        print("-----------------动物吃--------------------")

    def drink(self):
        print("-----------------动物喝--------------------")

    def sleep(self):
        print("-----------------动物睡觉------------------")

    def run(self):
        print("-----------------动物跑--------------------")

class Dog(Animal):
    def bark(self):
        print("------------------狗汪汪叫-----------------")

class Xiaotq(Dog):
    def fly(self):
        print("-------------------哮天犬飞----------------")

xiaotq = Xiaotq()
xiaotq.fly()
xiaotq.bark()
xiaotq.eat()