"""
Author: Damian Archer
Date: 1/10/2023
File: InheritanceAndCompositionExercise.py
Purpose: PCPP Certification Exercises
"""

import abc

# Tires inherits abstract base class 
class Tires(abc.ABC):
    def __init__(self, size):
        self.__size = size
        self.__pressure = 29

    def pump(self, pressure):
        self.pressure = pressure
        return f'Pumped tire pressure to {pressure}'
        
    @property
    def pressure(self):
        return self.__pressure
        
    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    @property
    def size(self):
        return self.__size

    @abc.abstractmethod # has abstract method 
    def type(self):
        pass

# subclass CityTires inherits superclass Tires
class CityTires(Tires):
    def __init__(self, size=15):
        super().__init__(size) # calls to superclass in initialization
        self.__type = 'city'
    
    @property # overrides abstract method type as a property
    def type(self):
        return self.__type
        
    
# subclass OffroadTires inherits superclass Tires
class OffroadTires(Tires):
    def __init__(self, size=18):
        super().__init__(size)
        self.__type = 'offroad'
        
    @property
    def type(self):
        return self.__type
        

class Engine:
    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type
    
    def start(self):
        self.__state = 1
        return f'Started the {self.fuel_type} engine'
    
    def stop(self):
        self.__state = 0
        return f'Stopped the {self.fuel_type} engine'

    def get_state(self):
        return f'{self.fuel_type} engine is ' \
               + ("running" if self.__state == 1 else "stopped")

# inherits Engine
class ElectricEngine(Engine):

    def __init__(self):
        super().__init__("electric")
        self.__state = 0


# inherits Engine
class PetrolEngine(Engine):

    def __init__(self):
        super().__init__("petrol")
        self.__state = 0

# Vehicle is has attributes VIN, engine, and tires
class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.__VIN = VIN
        self.__engine = engine
        self.__tires = tires

    @property
    def VIN(self):
        return self.__VIN

    @property
    def engine(self):
        return self.__engine

    @property
    def tires(self):
        return self.__tires

# CityCar inherits Vehicle, and
# is composed of an ElectricEngine and CityTires
class CityCar(Vehicle):
    def __init__(self):
        super().__init__(123434321, ElectricEngine(), CityTires())

    def __repr__(self):
        return "CityCar"

# AllTerrainCar inherits Vehicle, and
# is composed of a PetrolEngine and OffroadTires
class AllTerrainCar(Vehicle):
    def __init__(self):
        super().__init__(432432234, PetrolEngine(), OffroadTires())

    def __repr__(self):
        return "AllTerrainCar"


    

for c in CityCar, AllTerrainCar:
    car = c()
    print("-"*30)
    print("Instantiated", car)
    print(car.engine.start())
    print(car.engine.get_state())
    print(car.engine.stop())
    print(car.engine.get_state())
    print("Engine seems to work fine...")
    print("Let's check the tires pressure..")
    print(car.tires.pressure)
    print("Hmm, seems a little low...")
    print(car.tires.pump(32))
    print("Checking pressure again: {}".format(car.tires.pressure))
    print("What kind of tires are these, anyways..?")
    print(f'Oh, I see, they are {car.tires.type} tires')
    



    
        
        
