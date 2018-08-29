# Doing ex40.0.py except defining variables to initialize a class instead of inputing raw data
class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)

happy_bday = ['Happy birthday to you,',
              'Happy birthday to you,',
              'Happy birthday dear person,',
              'Happy birthday to you!']

scoop = ['Woopdidy scoop.',
         'Scoopity woop',
         'Poopity scoop',
         'Poop scoop,',
         'Scoopity poop poop']

birthday = song(happy_bday)
kanye = song(scoop)

birthday.sing()

kanye.sing()
