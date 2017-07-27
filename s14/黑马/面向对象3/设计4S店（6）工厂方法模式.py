__author = "Hu Rongyang"

class Store(object):
    def select_car(self):
        pass

    def order(self,car_type):
        return self.select_car(car_type)

class BMWCarStore(Store):#宝马店
    def select_car(self,car_type):
        return BMWFactory().select_car_by_type(car_type)

class BMWFactory():
    def select_car_by_type(self,car_type):
        pass
        # if car_type == "mini":
        #     return Suonata()
        # elif car_type == "720Li":
        #     return Mintu()
        # elif car_type == "X6":
        #     return Ix35()

bmw_store = BMWCarStore()
bmw = bmw_store.order("X6")

class XianDaiCarStore(Store):#现代店
    def select_car(self,car_type):
        return XianDaiFactory().select_car_by_type(car_type)

class XianDaiFactory():
    def select_car_by_type(self,car_type):
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

car_store = XianDaiCarStore()#创建现代4S店铺
car = car_store.order("索纳塔")#car就指向了Suonata()的实例对象
car.move()
car.music()
car.stop()
