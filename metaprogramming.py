"""
Author: Damian Archer
Date: 1/3/2023
File: metaprogramming.py
Purpose: PCPP Exercises - Metaprogramming
"""


from datetime import datetime
import time

# function to return class variable "instantiation_time"
def get_instantiation_time(self):
    return self.instantiation_time

# metaclass to timestamp classes
class Time_Stamper(type):
    classes = []                                            # list of classes instantiated with metaclass.
    def __new__(mcs, name, bases, dictionary):
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
            
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now()
        
        time.sleep(0.00001) # used here to make instantiation time differences clearer in example

        if name not in mcs.classes:
            mcs.classes.append(name)

        return obj


class Cat(metaclass=Time_Stamper):
    def meow(self):
        return "legacy meow"

class Dog(metaclass=Time_Stamper):
    def wag(self):
        return "legacy wag"

class Mouse(metaclass=Time_Stamper):
    def squeek(self):
        return "legacy squeek"


meta_cat = Cat()
meta_dog = Dog()
meta_mouse = Mouse()

print(meta_mouse.squeek())
print(meta_mouse.get_instantiation_time())

print(meta_dog.wag())
print(meta_dog.get_instantiation_time())

print(meta_cat.meow())
print(meta_cat.get_instantiation_time())


print("Classes using", Time_Stamper.__name__, "class for instantiation:", Time_Stamper.classes)



