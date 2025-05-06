from animal import Animal

class Mammal(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> None:
        result = 'Mammals give birth to live young and raise them until they can be independent. '
        return super().reproduce() + result

    def __repr__(self):
        text = '\nClass: Mammal'
        return super().__repr__() + text