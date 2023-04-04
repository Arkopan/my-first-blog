class Descriptor:

    def __init__(self) -> None:
        self.__fuel_capacity = 0

    def __get__(self,obj,obj_type):
        return self.__fuel_capacity

    def __set__(self,obj,value):
        if isinstance(value,int):
           print(value)
        else:
            raise TypeError('Fuel capacity can only be an integer')
        
        if value<0:
            raise ValueError('Fuel capacity can never be less or equal to zero')

        self.__fuel_capacity = value


    def __delete__(self,obj):
        del self.__fuel_capacity



class Car:
    fuel_capacity = Descriptor()

    def __init__(self, model, color, fuel_capacity) -> None:
        self.model = model
        self.color = color
        self.fuel_capacity = fuel_capacity

    def method(self):
        pass

car1 = Car('BMW', 'red', 50)

print(car1.fuel_capacity)

#car1.fuel_capacity = 10.4

car1.fuel_capacity = 100

print(car1.method)
print(Car.method)