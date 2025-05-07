from pet import Pet
from carnivore import Carnivore
from mammal import Mammal

class Dog(Mammal, Carnivore, Pet): # method resolution order (if its not in mammal, then go to herbivore, etc.)
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs) # doesn't need self
        self.ears = ears

    def __repr__(self):
        text = '\nSpecies: Dog'
        result = Mammal.__repr__(self) + text  # Add Mammal info
        result += '\n' + Pet.__repr__(self)  # Add Pet info
        result += '\n' + Carnivore.__repr__(self)  # Add Carnivore info
        return result
    
    def reproduce(self) -> None:
        mammal = Mammal.reproduce(self)  # this must return a string
        dog = 'Dogs grunt and hump like Chop.'
        print(mammal + dog)

    def move(self) -> None:
        print('I move by trotting a two-beat gait where diagonal pairs of legs move together.')

    def sleep(self) -> None:
        print('Dogs are not nocturnal or diurnal. Instead, they are known more as social sleepers.')
        
    def eat(self) -> None:
        Carnivore.eat(self)

    def pet(self):
        pet = Pet.pet(self)
        print(pet)

if __name__ == '__main__':
    b1 = Dog()
    print()
    print(repr(b1))
    print()
    b1.reproduce()
    print()
    b1.eat()
    print()
    b1.move()
    print()
    b1.sleep()
    print()
    b1.pet()
    print()
