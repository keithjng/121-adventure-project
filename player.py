import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.equipment = []
        self.equipStren = 0
        self.effects = []
        self.health = 100
        self.alive = True
        self.armor = 0
        self.money = 30
        self.score = 0
        self.npcVisits = 0
        self.win = False
    def showStats(self):
        print()
        print("Name:", self.character)
        print("HenPoints (HP):", self.health)
        print("Armor:", self.armor)
        print("Hubucks:", self.money)
        print("Strength:", self.strength)
        print("Intelligence:", self.intelligence)
        print("Monsters killed:", self.score)
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        print("These items are equipped:")
        print()
        for i in self.equipment:
            print(i.name)
        print()
        input("Press enter to continue...")
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def itemInfo(self, item):
        clear()
        print("Here's some information about", item.name)
        print()
        item.describe()
        print()
        input("Press enter to continue...")
    def attackMonster(self, mon):
        attacking = True
        while attacking == True:
            clear()
            print("You are attacking " + mon.name)
            print()
            print("You have " + str(self.health) + " HenPoints.")
            print(mon.name + " has " + str(mon.health) + " HenPoints.")
            print()
            pDamage = self.strength + self.equipStren
            print("You attack for", pDamage)
            print(mon.name + " attacks for " + str(mon.strength))
            monDamage = mon.strength
            damageReduc = max(0, monDamage - self.armor)
            randNum = random.randint(1, 10)
            if randNum <= self.intelligence:
                print("You evaded the attack!")
            else:
                self.health = self.health - damageReduc
            mon.health = mon.health - pDamage
            if self.health <= 0:
                dead = True
                for item in self.equipment:
                    if item.name == "Life Vest":
                        self.health += monDamage
                        self.equipment.remove(item)
                        self.items.remove(item)
                        print("You took a lethal blow but you were saved by your Life Vest!")
                        dead = False
                        if mon.health <= 0:
                            print("\n")
                            print("You win. You now have " + str(self.health) + " HenPoints.")
                            print("You got", mon.money, "Hubucks from the", mon.name)
                            self.score += 1
                            attacking = False
                            if mon.loot != None:
                                mon.loot.putInRoom(self.location)
                            mon.die(self)
                        else:
                            print("You rush out of combat.")
                            attacking = False
                if dead == True:
                    print("You lose.")
                    attacking = False
                    self.alive = False
            elif mon.health <= 0:
                print("\n")
                print("You win. You now have " + str(self.health) + " HenPoints.")
                print("You got", mon.money, "Hubucks from ", mon.name)
                self.score += 1
                attacking = False
                if mon.loot != None:
                    mon.loot.putInRoom(self.location)
                mon.die(self)
            print()
            if attacking == False:
                input("\nPress enter to continue")
            elif attacking == True:
                decision = input("Type \"escape\" if you have a rope to use, otherwise, the battle continues! ")
                if decision.strip().lower() == "escape":
                    for item in self.items:
                        if item.name == "Rope":
                            print("\nYou escaped!\n")
                            input("Press enter to continue")
                            self.items.remove(item)
                            attacking = False

class Henry(Player):
    def __init__(self):
        self.character = "Henry"
        self.strength = 6
        self.intelligence = 4
        Player.__init__(self)

class Hubert(Player):
    def __init__(self):
        self.character = "Hubert"
        self.strength = 8
        self.intelligence = 2
        Player.__init__(self)
