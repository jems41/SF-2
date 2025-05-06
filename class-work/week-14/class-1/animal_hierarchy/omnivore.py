from heterotroph import Heterotroph

class Omnivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat anything!')

    def __repr__(self) -> str:
        text = 'This organism is an omnivore, it can feed on both plants and other animals.'
        return super().__repr__() + text