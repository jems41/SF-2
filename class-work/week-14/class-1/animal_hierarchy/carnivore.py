from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat meat.')

    def __repr__(self) -> str:
        text = 'This organism is carnivore. It feeds on other animals, and its physical features facilitates hunting.'
        return super().__repr__() + text