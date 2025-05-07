from animal import Animal

class Bird(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> str:
        fishReproduce = 'Birds typically reproduce by hatching and \
incubating their eggs. '
        return super().reproduce() + fishReproduce

    def __repr__(self):
        fishInfo = '\nClass: Bird'
        return super().__repr__() + fishInfo
    