from animal import Animal # question when do i use abstract class?

class Fish(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> None:
        result = 'Fish reproduction varies largely, some give birth to live young while others lay eggs.'
        super().reproduce()
        print(result)

    def __repr__(self):
        text = '\nClass: Fish'
        return super().__repr__() + text
    