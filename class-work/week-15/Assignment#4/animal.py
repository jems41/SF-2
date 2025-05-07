from abc import ABCMeta, abstractmethod # i really dont want this object to be created i just want it as a blueprint

class Animal(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    @abstractmethod # only needs at least one abstract method to be an abstract class
    def move(self) -> None:
        pass

    @abstractmethod
    def sleep(self) -> None:
        pass

    def reproduce(self) -> str:
        return 'Members of this kingdom reproduce by finding a mate \
of the same species. '
    
    def __repr__(self) -> str:
        return f'Kingdom: Animalia'
    
# if __name__ == '__main__': # cant instantiate abstract class Animal without an implementation for abstract methods
#     anim = Animal(6)