__author = "Hu Rongyang"
class CarStore():
    def order(self,car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mintu()
        elif car_type == "ix35":
            return Ix35()

class Car():
    def move(self):
        print("车在移动...")
    def music(self):
        print("正在播放音乐...")
    def stop(self):
        print("车在停止...")

class Suonata(Car):#索纳塔
    pass

class Mintu(Car):#名图
    pass

class Ix35(Car):
    pass

car_store = CarStore()#创建4S店铺
car = car_store.order("索纳塔")#car就指向了Suonata()的实例对象
car.move()
car.music()
car.stop()
