from pet import Pet
from omnivore import Omnivore
from mammal import Mammal

class Dog(Mammal, Omnivore, Pet): # method resolution order (if its not in mammal, then go to herbivore, etc.)
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs) # doesn't need self
        self.ears = ears

    #                 {{ Animal [Kingdom: Animalia]
    # Mammal.__repr__ {{ Mammal [Class: Mammal]
    #                  { Bunny {Species: Dog}
    #                  { Pet {This animal is a pet}

    def __repr__(self):
        text = '\nSpecies: Bunny'
        result = Mammal.__repr__(self) + text # kingdom, class, species
        result = '\n' + Pet.__repr__(self) # pet info
        return result + '\n' + Omnivore.__repr__(self) # updated to omnivore
    
    def reproduce(self) -> None:
        super().reproduce()

    def move(self) -> None:
        print('I move by trotting A two-beat gait where diagonal pairs of legs move together.')

    def sleep(self) -> None:
        print('Dogs are not nocturnal or diurnal. Instead, they are known more as social sleepers.')
        
    def eat(self) -> None:
        Omnivore.eat(self)
        print('Dogs are classified as omnivores, which means they can satisfy their nutritional needs by consuming both meat and plant-based foods.')
        
if __name__ == '__main__':
    b1 = Dog()
    print(b1.__repr__())

    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

    print()
    b1.eat

    print()
    print(b1.pet())

    