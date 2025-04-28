from animal import Animal

class Mammal(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> None:
        result = 'Mammals give brith to live young and raise them until they can be independent'
        super().reproduce()
        print(result)

    def __repr__(self):
        text = '\nClass: Mammal'
        return super().__repr__() + text