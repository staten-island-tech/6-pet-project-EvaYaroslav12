# Personal Pet Project
# You will be designing an application to allow users to play with a new “pet”. Think Tamgaotchi. You may use whatever lore or character style you want.
# Users will be able to create a new pet based on Python classes. After instantiating a new pet they will be able to play and care for the pet. Values for the pet should be displayed and updated. See in class example.
class pet:
    def __init__(self, name, satiety, energy, happiness, daylived):
        self.name = name
        self.satiety = satiety
        self.energy = energy
        self.happiness = happiness
        self.daylived = daylived

    def feed(self):
        self.satiety += 80

    def sleep(self):
        self.energy += 80
    
    def play(self):
        self.happiness += 40
        
    def liveaday(self):
        self.daylived += 1
        self.satiety -= 40
        self.energy -=35
        self.happiness -=10

    def alive(self):
        if self.satiety <= 0:
            print (self.name, "died because you were too poor to feed him.")
            return False
        if self.satiety >= 200:
            print (self.name, 'blew up.')
            return False
        if self.energy <= 0:
            print (self.name, 'died from sleep deprivation.')
            return False
        if self.energy >=200:
            print (self.name, 'began running so fast they set themselves on fire')
            return False
        if self.happiness <= 0:
            print (self.name, "died of depression.")
            return False
        if self.happiness >=200:
            print (self.name, "died laughing")
            return False
        else:
            return True
    
    def VitalsCheck(self):
        if self.satiety > 100:
            print ('what have you done im fat now.')
        if self.satiety == 100:
            print ('You have done a good job in feeding me, mortal.')
        if self.satiety < 100 and self.satiety > 40:
            print ('You have done an adequate job in feeding me, mortal.')
        if self.satiety <= 40 and self.satiety > 0:
            print ('Are you too broke to feed me??')

        if self.energy > 100 and self.happiness <= 20:
            print ('Im still depressed but at least im fast now')

        if self.energy > 100:
            print ('Guess im fast now')
        if self.energy == 100:
            print ('wow im actually perfectly rested :O')
        if self.energy < 100 and self.energy >35:
            print ('You have done an adequate job of shuting up and allowing me to rest.')
        if self.energy <= 35 and self.energy > 0:
            print ('Can you shush and let me sleep, mortal?')

        if self.happiness > 100:
            print ('Wow you love etertaining me dont you? you\'re like my personal jester.')
        if self.happiness == 100:
            print ('I am satisfied with your entertainment.')
        if self.happiness < 100 and self.happiness > 10:
            print ('You have done an adequate job of entertaining me.')
        if self.happiness <=10 and self.happiness >0:
            print ('Plebian, do you consider yourself so mighty that you dont feel the need to entertain me?')



petname = input('what do you want to name your pet? ')

Bast = pet(petname, 100, 100, 100, 0)
while Bast.alive() == True:
    Bast.liveaday()
    action = input ('Do you want to do anything today? [F]eed, [S]leep, [P]lay, [Enter] to skip ')
    actionlc = action.lower()
    if actionlc == 'f':
        Bast.feed()
    if actionlc == 's':
        Bast.sleep()
    if actionlc == 'p':
        Bast.play()
    Bast.VitalsCheck()

print(Bast.name, 'Is dead! They lived for', Bast.daylived, 'days')