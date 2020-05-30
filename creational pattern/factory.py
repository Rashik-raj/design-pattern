class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "woof!!!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "meow!!!"

def get_pet(pet='dog'):
    pets = dict(dog=Dog('tucker'),cat=Cat('simba'))
    return pets[pet]

dog = get_pet('dog')
cat = get_pet('cat')
print(dog.speak())
print(cat.speak())