import random
import updater
from item import Weapon
from item import Armor
from item import Item

class Monster:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.type = "monster"
        room.addMonster(self)
        updater.register(self)
        if self.name == "Germ":
            randomNum = random.randint(1, 4)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
        elif self.name == "Dust Ball":
            randomNum = random.randint(5, 8)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
            self.loot = Monster.lootChance(self)
        elif self.name == "Oil Blot":
            randomNum = random.randint(9, 12)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
            self.loot = Monster.lootChance(self)
        elif self.name == "Coffee Grounds":
            randomNum = random.randint(13, 16)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
            self.loot = Monster.lootChance(self)
        elif self.name == "Plastic Fork":
            randomNum = random.randint(17, 20)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
            self.loot = Monster.lootChance(self)
        elif self.name == "Dirty Dish":
            randomNum = random.randint(21, 24)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
            self.loot = Monster.lootChance(self)
        elif self.name == "Stained Pillow":
            randomNum = random.randint(25, 28)
            self.health = randomNum
            self.strength = randomNum // 2
            self.money = randomNum
            self.loot = Monster.lootChance(self)
        elif self.name == "Germ Cluster":
            self.health = 20
            self.strength = 5
            self.money = 20
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
        elif self.name == "Vacuum Bag":
            self.health = 30
            self.strength = 10
            self.money = 30
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
        elif self.name == "Grease Jar":
            self.health = 40
            self.strength = 15
            self.money = 40
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
        elif self.name == "Coffee Cup":
            self.health = 50
            self.strength = 20
            self.money = 50
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
        elif self.name == "Plastic Knife":
            self.health = 60
            self.strength = 25
            self.money = 60
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
        elif self.name == "Dishwasher":
            self.health = 70
            self.strength = 30
            self.money = 70
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
        elif self.name == "Soiled Couch":
            self.health = 80
            self.strength = 35
            self.money = 80
            self.loot = Item("Quarter", "You need 7 of these to do laundry!")
    def update(self):
        if random.random() > 1:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self, player):
        player.money += self.money
        self.room.removeMonster(self)
        updater.deregister(self)
    def spawnMonster(room):
        randMon = random.randrange(20)
        if randMon < 4: #4/20
            mon = "Germ"
        elif randMon < 8: #4/20
            mon = "Dust Ball"
        elif randMon < 11: #3/20
            mon = "Oil Blot"
        elif randMon < 14: #3/20
            mon = "Coffee Grounds"
        elif randMon < 17: #2/20
            mon = "Plastic Fork"
        elif randMon < 19: #2/20
            mon = "Dirty Dish"
        elif randMon < 20: #2/20
            mon = "Stained Pillow"
        spawnChance = random.randrange(4)
        if randMon < 3: # 3/4 chance it spawns
            Monster(mon, room)
    def lootChance(self):
        randNum = random.randint(1, 10) # 1/10 chance monster drops an item
        if self.name == "Germ":
            if randNum == 10:
                return Weapon("Wooden Sword", "Looks like a training sword.")
            else:
                return None
        elif self.name == "Dust Ball":
            if randNum == 10:
                return Weapon("Wooden Sword", "Looks like a training sword.")
            else:
                return None
        elif self.name == "Oil Blot":
            if randNum == 10:
                return Armor("Mask", "Protects you from viruses, everyone should wear one!")
            else:
                return None
        elif self.name == "Coffee Grounds":
            if randNum == 10:
                return Weapon("Stone Sword", "Is it made from cobblestone?")
            else:
                return None
        elif self.name == "Plastic Fork":
            if randNum == 10:
                return Armor("Small Shirt", "A red shirt with a bird-lion hybrid creature on it!")
            else:
                return None
        elif self.name == "Dirty Dish":
            if randNum == 10:
                return Weapon("Iron Sword", "The strongest weapon there is!")
            else:
                return None
        elif self.name == "Stained Pillow":
            if randNum == 10:
                return Weapon("Iron Sword", "The strongest weapon there is!")
            else:
                return None

class Boss(Monster):
    def __init__(self, name, room):
        self.type = "boss"
        Monster.__init__(self, name, room)
