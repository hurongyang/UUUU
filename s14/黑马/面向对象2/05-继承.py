__author = "Hu Rongyang"
class Animal:
    def eat(self):
        print("-----------------吃------------------")

    def drink(self):
        print("-----------------喝------------------")

    def sleep(self):
        print("-----------------睡觉------------------")

    def run(self):
        print("-----------------跑------------------")

class Dog(Animal):
    def bark(self):
        print("------------------狗汪汪叫-----------------")

class Cat(Animal):
    def catch(self):
        print("------------------猫抓老鼠-----------------")


a = Animal()
a.eat()

wangcai = Dog()
wangcai.eat()
wangcai.bark()

tom = Cat()
tom.eat()
tom.catch()