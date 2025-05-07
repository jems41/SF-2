from animal import Animal # question when do i use abstract class?

class Amphibian(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> None:
        amphibianReproduce = 'Amphibians reproduce by laying soft eggs in the water. '
        return super().reproduce() + amphibianReproduce

    def __repr__(self):
        amphibianInfo = '\nClass: Amphibian'
        return super().__repr__() + amphibianInfo