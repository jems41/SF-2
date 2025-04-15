class Animal:
    def __init__(self, legs=0):
        self.legs = legs
    
    def walk(self) -> None:
        print(f'This animal walks on their {self.legs} legs')
    
    def sleep(self) -> None:
        print(f'Different animals have different sleeping habits')

    def __repr__(self) -> str:
        return f'Animal no idea \nLegs: {self.legs}'

if __name__ == '__main__': # is this current script that im running the animal class
    anim = Animal(6)
    print(anim)

    print()
    anim.walk()
    anim.sleep()
