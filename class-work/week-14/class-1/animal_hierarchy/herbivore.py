from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat plants')

    def __repr__(self) -> str:
        text = 'This organism is herbivore. It feeds on plant matter and its physiology \
            facilitates food search.'
        return super().__repr__() + '\n' + text
    
if __name__ == "__main__":
    herbivore = Herbivore()
    herbivore.eat()
    print(repr(herbivore))