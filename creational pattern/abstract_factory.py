class Dog:
    def speak(self):
        return "Woof!!!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """ concrete factory """
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class PetStore:
    """ abstract factory """

    def __init__(self,pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        """ utility method to show detail """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print('our pet is {}'.format(pet))
        print('our pet says hello by {}'.format(pet.speak()))
        print('Its food is {}'.format(pet_food))

#create a concreate factory
factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()