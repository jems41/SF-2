from pet import Pet
from herbivore import Herbivore
from mammal import Mammal

class Bunny(Mammal, Herbivore, Pet): # method resolution order (if its not in mammal, then go to herbivore, etc.)
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs) # doesn't need self
        self.ears = ears

    #                 {{ Animal [Kingdom: Animalia]
    # Mammal.__repr__ {{ Mammal [Class: Mammal]
    #                  { Bunny {Species: Bunny}
    #                  { Pet {This animal is a pet}

    def __repr__(self):
        text = '\nSpecies: Bunny'
        result = Mammal.__repr__(self) + text # kingdom, class, species
        result = '\n' + Pet.__repr__(self) # pet info
        return result + '\n' + Herbivore.__repr__(self) # herbivore
    
    def reproduce(self) -> None:
        super().reproduce()
        print('Bunnies can produce multiple litter per year potentially having 3-8 kits per litter')

    def move(self) -> None:
        print('I move by hopping and I can see things behind me')

    def sleep(self) -> None:
        print('Bunnies as nocturnal animals, typically sleep around 12 to 14 hours a day in short, intermittent\
              periods')
        
    def eat(self) -> None:
        Herbivore.eat(self)
        print('I mostly eat fresh hay and grass, with some leafy greens\
              and a few pellets. I should only be given fruit and root\
              vegetables, like carrots, as occassional treat')
        
if __name__ == '__main__':
    b1 = Bunny()
    
    print()
    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

    print()
    b1.eat

    print()
    print(b1.pet())

    