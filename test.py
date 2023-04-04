import random
import statistics
from datetime import date


import functools
def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)
print(summator.__name__)

class Planet:
    count = 0

    def __new__(cls,*args,**kwargs):
        print('__new__ called')
        obj = super().__new__(cls)
        return obj

    def __init__(self,name,population=None) -> None:
        self.name = name
        self.population = population or []
        print('__init__ called')
        Planet.count+=1
    
    def __repr__(self) -> str:
        return f'Planet {self.name}'
    
    def __str__(self) -> str:
        return self.name
    
    def add_human(self,human):
        print(f'Welcome {human.name} on planet {self.name}!')
        self.population.append(human)

    
class Human:
    def __init__(self,name=str,age=int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'Human {self.name}'
    
    def _say(self,text):
        print(text)
    
    def say_name(self):
        self._say(f'Hi my name is {self.name}')

    def say_age(self):
        self._say(f'Hi my age is {self.age}')
    

solar_system = []

planet_names = ['Mecury', 'Venus', ' Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)

earth = Planet('Earth')
print(earth)
print(earth.name)
print(Planet.count)

Bob = Human('Bob',35)
earth.add_human(Bob)
print(earth.population)
Bob.say_age()
Bob.say_name()


class Event:

    def __init__(self,description,event_date) -> None:
        self.description = description
        self.event_date = event_date
    
    def __str__(self) -> str:
        return (f'Event \'{self.description}\' at {self.event_date}')
    
event_description = 'Print something'
event_date = date.today()

event = Event(event_description,event_date)

print(event)


class Robot:

    def __init__(self, power) -> None:
        self._power = power

    power = property()

    @power.setter
    def power(self,value):
        if value>=0:
            self._power=value
        else:
            self._power=0

    @power.getter
    def power(self):
        return self._power
    
    @power.deleter
    def power(self):
        print('Make robot useless')
        del self._power

wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)

del wall_e.power

    
