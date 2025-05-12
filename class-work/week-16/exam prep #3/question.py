"""
Type: Long Answer
Topic: Object-oriented programming : classes, abstract classes, inheritance, 
constructors and method overloading

An orchestra is made up of instruments. Each instrument can play a sound and 
the orchestra "has" instruments. The orchestra can also manage its instruments 
by adding them and then performing them.

Your task is to create first an abstract parent class called Instruments with the following:
   - A constructor that takes a parameter called name and assigns it to an instance
     variable called self.name.
   - An abstract method called play_sound that returns None.

Next, create two child classes that inherit from Instruments:
1. StringInstrument
    - Implement __repr__ to return the instrument type (you could hard-code this) and 
      "Instrument: {name}".
    - play_sound method that returns the string "Vibrations of strings"
2. WoodwindInstrument
    - Implement __repr__ to return the instrument type (you could hard-code this) and 
      "Instrument {name}".
    - play_sound method that returns the string "Resonant breathy tones"
    
Lastly, create a class called Orchestra that has the following:
   - An instance variable called instruments that is initialized as an empty list.
   - A method called add_instrument that takes an instrument object as a parameter 
     and adds it to the instruments list.
   - A method called perform that iterates through the instruments list and calls the
     play_sound method of each instrument, returning a list of the sounds made by 
     the instruments.

With input StringInstrument("Violin"), WoodwindInstrument("Flute") with proper orchestra input
and __repr__ for both instruments, the output should look like this:

Instrument Type: String
Instrument Name: Violin
Instrument Type: Woodwind
Instrument Name: Flute
['Vibrations of strings', 'Resonant breathy tones']
"""
