from animal import Animal

class Fish(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> str:
        fishReproduce = 'Fish reproduction varies largely, some give birth to live young while others lay eggs. '
        return super().reproduce() + fishReproduce

    def __repr__(self):
        fishInfo = '\nClass: Fish'
        return super().__repr__() + fishInfo
    