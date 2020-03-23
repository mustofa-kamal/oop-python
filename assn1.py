import random


class Setup(object):
    def __init__(self): pass

    def print_inventory(self):
        print('current inventory:')
        for i, x in enumerate(self.inventory):
            print(f'{i + 1}. {x}')


class ModeEasyHero(Setup):
    def __init__(self, inventory=["sword"]):
        Setup.__init__(self)
        self.inventory = inventory


class ModeDifficultHero(ModeEasyHero):
    def __init__(self, inventory=["diamonds", "gold", "silver", "sword"]):
        ModeEasyHero.__init__(self)
        self.inventory = inventory

    def add_inventory(self):
        print('Add new inventory. Enter space separated inventory:')
        self.inventory.extend(list(input().split()))

    def print_special_combination_to_defeat_enemy(self):
        print('Special combination to defeat enemy:')
        combination = random.sample(self.inventory, k=3)
        for i, x in enumerate(combination):
            print(f'{i + 1}. {x}')


class MainApplication(ModeDifficultHero):

    def handle_mode_easy_hero(self):
        print('*************** You are in easy mode ******************')
        print('In this easy mode, you can only print current inventory')
        h = ModeEasyHero()
        h.print_inventory()

    def handle_mode_difficult_hero(self):
        print('*************** You are in difficult mode ******************')
        print('In this difficult mode, you can print current inventory, add new inventory, print special combination to defeat enemies')
        s = ModeDifficultHero()
        user_input = input(
            '\nWhat you want to do:\n1: Print current inventory\n2: Add new inventor\n3: print special combination to defeat enemies\nEnter:\n')

        if user_input == '1':
            s.print_inventory()
        elif user_input == '2':
            s.add_inventory()
            s.print_inventory()
        elif user_input == '3':
            s.print_special_combination_to_defeat_enemy()

    def __init__(self):

        menuchoices = {
            "1": self.handle_mode_easy_hero,
            "2": self.handle_mode_difficult_hero,
            '0': quit
        }

        while True:

            user_input = input(
                '\nPlease enter 0 - 2\n1: mode easy (You can not add new inventory)\n2: mode difficult (You can add new inventory and print special combination to defeat enemies)\n0: Quit\n\nEnter:')

            if user_input == '':
                print("Please Enter 0 - 2:")
            elif user_input == '0':
                print('Good Bye!')
                break
            else:
                menuchoices[user_input]()


print('***************************')
print('Welcome to Hero!')
print('***************************')

my_app = MainApplication()
