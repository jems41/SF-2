from animal import Animal

class Amphibian(Animal):
    def reproduce(self) -> None:
        amphibianReproduce = 'Amphibians reproduce by laying soft \
eggs in the water. '
        return super().reproduce() + amphibianReproduce

    def __repr__(self):
        amphibianInfo = '\nClass: Amphibian'
        return super().__repr__() + amphibianInfo