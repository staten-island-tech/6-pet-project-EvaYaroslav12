# Personal Pet Project
# You will be designing an application to allow users to play with a new “pet”. Think Tamgaotchi. You may use whatever lore or character style you want.
# Users will be able to create a new pet based on Python classes. After instantiating a new pet they will be able to play and care for the pet. Values for the pet should be displayed and updated. See in class example.
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

kris = Hero('Kris', 190, ['potion'])
kris.buy({'title':'Sword', 'atk': 34})
print(kris.__dict__) 

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

BankAccount.show_balance(kris)