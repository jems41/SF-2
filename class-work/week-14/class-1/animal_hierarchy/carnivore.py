from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def __repr__(self):
        text = 'This organism is a carnivore. If feeds on other animals, and its physical features facilitates hunting.'
        return super().__repr__() + '\n' + text
    
    def eat(self):
        super().eat()
        print('I eat meat.')

if __name__ == '__main__':
    carnivore = Carnivore()
    print(repr(carnivore))
    carnivore.eat()