from animal import Animal # question when do i use abstract class?

class Reptile(Animal): # mammal is an abstract class and will become an abstract will overwrite animal.py
    def reproduce(self) -> None:
        text = 'Reptiles reproduce by laying eggs, typically on land rather than water.'
        super().reproduce()
        print(text)

    def __repr__(self):
        text = '\nClass: Reptile'
        return super().__repr__() + text
    