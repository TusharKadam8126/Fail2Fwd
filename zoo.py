class Animal:
    def __init__(self,make_sound):
        self.make_sound = make_sound
        print("Different animal sounds are there.")
class Dog:
    def __init__(self,make_sound):
        self.make_sound = make_sound
        print("Dog says :" + make_sound)
class Cat:
    def __init__(self,make_sound):
        self.make_sound = make_sound
        print("Cat says :" + make_sound)
class Cow:
    def __init__(self,make_sound):
        self.make_sound = make_sound
        print("Cow says :" + make_sound)
obj1 = Dog("Woof!")
obj2 = Cat("Meow!")
obj3 = Cow("Moo!")


           