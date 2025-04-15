from animal import Animal

class Cat(Animal): # inheriting from animal
    def __init__(self):
        super().__init__(4) # build from animal
        self.type = 'cat'

    def sleep(self, hours = None) -> None:
        if hours == None:
            print('Cats sleep in warm and comfortable places')
        else:
            print(f'Cats can sleep for {hours} hours daily')

    def __repr__(self) -> str:
        return f'Animal: {self.type} \nLegs: {self.legs}'
    
cat = Cat()
print(cat)  # Animal: cat \n Legs: 4

print()

cat.walk()
cat.sleep()
cat.sleep(12)