from animal import Animal

class Fish(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> str:
        result = 'Fish reproduction varies largely, some give birth to live young while others lay eggs.'
        return super().reproduce() + result

    def __repr__(self):
        text = '\nClass: Fish'
        return super().__repr__() + text
    