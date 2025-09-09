class Vehicle:
    def __init__(self,start_engine,move,stop_engine):
        self.start_engine = start_engine
        self.move = move
        self.stop_engine = stop_engine
class Car(Vehicle):
    def method1(self):
        print("Car engine started." + self.start_engine)
        print("Car can move." + self.move)
        print("Car engine stopped." + self.stop_engine)
class Bike(Vehicle):
    def method2(self):
        print("Bike engine started." + self.start_engine)
        print("Bike can move." + self.move)
        print("Bike engine stopped." + self.stop_engine)
class Truck(Vehicle):
    def method3(self):
        print("Truck engine started." + self.start_engine)
        print("Truck can move." + self.move)
        print("Truck engine stopped." + self.stop_engine) 
myobj1 = Car()
myobj2 = Bike()
myobj3 = Truck()
myobj1.Car()
myobj2.Bike()
myobj3.Truck()