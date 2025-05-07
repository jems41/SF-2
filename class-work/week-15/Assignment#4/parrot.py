from pet import Pet
from omnivore import Omnivore
from bird import Bird

class Parrot(Bird, Omnivore, Pet): # method resolution order (if its not in mammal, then go to herbivore, etc.)
    def __init__(self, legs = 2, wings = 2, colour='yellow'):
        super().__init__(legs) # doesn't need self
        self.wings = wings
        self.colour = colour

    def __repr__(self):
        text = '\nSpecies: Parrot'
        result = Bird.__repr__(self) + text
        result += '\n' + Pet.__repr__(self)
        result += '\n' + Omnivore.__repr__(self)
        return result
    
    def reproduce(self) -> None:
        mammalReproduce = Bird.reproduce(self)
        parrotReproduce = 'Parrots often take a few days to lay a \
full clutch of eggs. This can be as many as three to four eggs.'
        print(mammalReproduce + parrotReproduce)

    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb \
and even use a unique method called \"beakiation\" to traverse narrow \
branches.')

    def sleep(self) -> None:
        print('Parrots sleep around 10 to 12 hours each night, often \
tucked under their wings. They may also take naps during the day.')
        
    def eat(self) -> None:
        Omnivore.eat(self)
        print('I eat both plant and animal matter. My natural diet \
includes a variety of food like seeds, nuts, fruits, vegetables, flowers, \
buds, and insects.')

if __name__ == '__main__':
    p1 = Parrot(2, 2)
    print()
    print(repr(p1))
    print()
    p1.reproduce()
    print()
    p1.eat()
    print()
    p1.move()
    print()
    p1.sleep()
    print()
    print(p1.pet() + '\n')

    p2 = Parrot(2, 2, 'red')
    print(p2)
