from player import Player
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc = None):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Weapon(Item):
    def __init__(self, name, desc = None):
        self.type = "Weapon"
        Item.__init__(self, name, desc)
        if self.name == "Wooden Sword" or self.name == "Sharpened Stick":
            self.strength = 5
            self.price = 30
        elif self.name == "Stone Sword" or self.name == "Pocket Knife":
            self.strength = 7
            self.price = 45
        elif self.name == "Iron Sword" or self.name == "Plane Shrapnel":
            self.strength = 10
            self.price = 60
    def describe(self):
        clear()
        print(self.desc)
        print("Strength:", self.strength)
        print("Value:", self.price, "Hubucks")
        print()
        input("Press enter to continue...")
    def equip(self, player):
        canEquip = True
        for item in player.equipment:
            if self.type == item.type:
                print("You already have a weapon equipped!")
                print("\n")
                input("Press enter to continue...")
                canEquip = False
        if canEquip == True:
            clear()
            print("You have equipped the", self.name)
            print("\n")
            input("Press enter to continue...")
            player.equipStren += self.strength
            player.equipment.append(self)
    def dequip(self, player):
        clear()
        print("You have dequipped the", self.name)
        print("\n")
        input("Press enter to continue...")
        player.equipStren -= self.strength
        player.equipment.remove(self)

class Armor(Item):
    def __init__(self, name, desc = None):
        self.type = "Armor"
        Item.__init__(self, name, desc)
        if self.name == "Cardboard Box":
            self.protection = 1
            self.price = 20
        elif self.name == "Duck Socks":
            self.protection = 2
            self.price = 40
        elif self.name == "Mask":
            self.protection = 3
            self.price = 60
        elif self.name == "Small Shirt":
            self.protection = 4
            self.price = 80
        elif self.name == "Life Vest":
            self.protection = 0
            self.price = 100
    def describe(self):
        clear()
        print(self.desc)
        print("Protection:", self.protection)
        print("Price:", self.price)
        print()
        input("Press enter to continue...")
    def equip(self, player):
        clear()
        print("You have equipped the", self.name)
        print("\n")
        input("Press enter to continue...")
        player.armor += self.protection
        player.equipment.append(self)
    def dequip(self, player):
        clear()
        print("You have dequipped the", self.name)
        print("\n")
        input("Press enter to continue...")
        player.armor -= self.protection
        player.equipment.remove(self)

class Consumable(Item):
    def __init__(self, name, desc = None):
        self.type = "Consumable"
        self.restores = 0
        self.strenBoost = 0
        self.intelBoost = 0
        self.price = 0
        self.durability = 0
        Item.__init__(self, name, desc)
        if self.name == "Dried Kelp":
            self.restores = 5
            self.price = 10
        elif self.name == "Bear Claw" or self.name == "Raw Cod" or self.name == "Beef Jerky":
            self.restores = 10
            self.price = 18
        elif self.name == "Cooked Salmon":
            self.restores = 30
            self.price = 50
        elif self.name == "Honey Bottle":
            self.strenBoost = 2
            self.durability = 5
            self.price = 20
        elif self.name == "Coffee":
            self.intelBoost = 2
            self.durability = 5
            self.price = 20
        elif self.name == "Bubble Tea":
            self.strenBoost = 1
            self.intelBoost = 1
            self.restores = 5
            self.durability = 5
            self.price = 30
        elif self.name == "Irradiated Pretzels":
            self.desc = "These are some wacky, green-colored pretzels! If you eat them, there is a chance that: \n- Your health is restored to full \n- Your stats are raised to full for 5 rooms \n- You lose 40 health :("
            self.durability = 5
            self.price = 50
        elif self.name == "Rope":
            self.desc = "Use this to escape from any combat situation!"
            self.price = 60
    def describe(self):
        clear()
        print(self.desc)
        print("Restores:", self.restores)
        print("Strength Boost:", self.strenBoost)
        print("Intelligence Boost:", self.intelBoost)
        print()
        input("Press enter to continue...")
    def eat(self, player):
        if self.name == "Irradiated Pretzels":
            randChance = random.randint(0, 2)
            if randChance == 0:
                print("You were healed to full.")
                input("\nPress enter to continue")
                player.health = 100
            elif randChance == 1:
                print("You now have full stats.")
                input("\nPress enter to continue")
                player.strength = 10
                player.intelligence = 10
                player.effects.append(self)
            elif randChance == 2:
                print("You take 40 damage!")
                input("\nPress enter to continue")
                player.health -= 40
                if player.health <= 0:
                    print("You lose.")
                    input("\nPress enter to continue")
                    self.alive = False
        else:
            player.health += self.restores
            player.health = min(100, player.health)
            player.strength += self.strenBoost
            player.strength = min(10, player.strength)
            player.intelligence += self.intelBoost
            player.intelligence = min(10, player.intelligence)
            player.effects.append(self)
            print("You ate the", self.name)
            input("\nPress enter to continue")
    def removeEffects(self, player):
        player.strength -= self.strenBoost
        player.intelligence -= self.intelBoost
