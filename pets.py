import json

class Pet:

    def __init__(self,name) -> None:
        self.name = name

class Dog(Pet):

    def __init__(self, name, breed=None) -> None:
        super().__init__(name)
        self.breed = breed

    def say(self):
        print(f'Dog {self.name} says: waw!')


class ExportJson:
    def to_json(self):
        return json.dumps({
            "name":self.name,
            "breed":self.breed
        })
    
class ExDog(Dog,ExportJson):
    def __init__(self, name, breed=None) -> None:
        super().__init__(name, breed)

class WoolenDog(Dog,ExportJson):
    def __init__(self,name,breed=None) -> None:
        super(Dog,self).__init__(name)
        self.breed = f'Woolen dog - breed {breed}'


dog1 = Dog('Sharik', 'Labrador')
print(dog1.name)
dog1.say()

dog2 = ExDog('Bobik','Doberman')
print(dog2.breed)
print(dog2.to_json())

dog3 = WoolenDog('Check','Bulldog')
print(dog3.breed)

