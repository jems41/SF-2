from abc import ABCMeta, abstractmethod

class Instruments(object, metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def play_sound(self) -> None:
        pass

class StringInstrument(Instruments):
    def __repr__(self):
        stringinstrument = f'Instrument Name: {self.name}'
        return 'Instrument Type: String' + '\n' + stringinstrument

    def play_sound(self):
        return 'Vibrations of strings'
    
class WoodwindInstrument(Instruments):
    def __repr__(self):
        woodwindinstrument = f'Instrument Name: {self.name}'
        return 'Instrument Type: Woodwind' + '\n' + woodwindinstrument

    def play_sound(self):
        return 'Resonant breathy tones'
    
class Orchestra:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def perform(self):
        sounds = []
        for instrument in self.instruments:
            sounds.append(instrument.play_sound())
        return sounds
    
if __name__ == '__main__':
    violin = StringInstrument("Violin")
    flute = WoodwindInstrument("Flute")

    orchestra = Orchestra()

    orchestra.add_instrument(violin)
    orchestra.add_instrument(flute)

    print(repr(violin))
    print(repr(flute))

    print(orchestra.perform())