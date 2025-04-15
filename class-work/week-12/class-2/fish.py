from __future__ import annotations

from animal import Animal
class Fish(Animal):
    def __init__(self, colour):
        super().__init__(0)
        self.type = 'fish'
        self.colour = colour

    def walk(self) -> None:
        print('Fish do not walk, they swim')

    def sleep(self) -> None:
        print('Fish rest by reducing their activity and metabolism')

    def __repr__(self) -> str:
        return f'Animal: {self.type} \nColour: {self.colour}'
    
    def changeColour(self, new_colour:str) -> None:
        self.colour = new_colour
        return

    def sameColour(self, other:Fish) -> bool:
        ''' return True if this Fish has same colour as other fish'''
        return self.colour == other.colour

if __name__ == '__main__':
    fish = Fish('blue')
    print(fish)

    print()

    fish.sleep()
    fish.walk()

    print()
    fish.changeColour('yellow black stripped')
    print(fish)

    fish2 = Fish('blue')
    fish.sameColour(fish2)