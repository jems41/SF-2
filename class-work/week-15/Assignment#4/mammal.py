from animal import Animal

class Mammal(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> None:
        mammalReproduce = 'Mammals give birth to live young and raise them until they can be independent. '
        return super().reproduce() + mammalReproduce

    def __repr__(self):
        mammalInfo = '\nClass: Mammal'
        return super().__repr__() + mammalInfo