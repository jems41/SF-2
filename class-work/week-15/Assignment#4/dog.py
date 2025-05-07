from pet import Pet
from omnivore import Omnivore
from mammal import Mammal

class Dog(Mammal, Omnivore, Pet): # method resolution order (if its not in mammal, then go to herbivore, etc.)
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs) # doesn't need self
        self.ears = ears

    def __repr__(self):
        text = '\nSpecies: Dog'
        result = Mammal.__repr__(self) + text
        result += '\n' + Pet.__repr__(self)
        result += '\n' + Omnivore.__repr__(self)
        return result
    
    def reproduce(self) -> None:
        mammalReproduce = Mammal.reproduce(self)
        dogReproduce = 'Dogs grunt and hump like Chop.'
        print(mammalReproduce + dogReproduce)

    def move(self) -> None:
        print('I move by trotting a two-beat gait where diagonal \
pairs of legs move together.')

    def sleep(self) -> None:
        print('Dogs are not nocturnal or diurnal. Instead, they are \
known more as social sleepers.')
        

if __name__ == '__main__':
    d1 = Dog()
    print()
    print(repr(d1))
    print()
    d1.reproduce()
    print()
    print(d1.eat())
    print()
    d1.move()
    print()
    d1.sleep()
    print()
    print(d1.pet())
    print()
