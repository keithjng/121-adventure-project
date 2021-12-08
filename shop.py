import random
import os
from item import Item
from item import Weapon
from item import Armor
from item import Consumable

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Shop:
    def __init__(self, room, roomChoice = None):
        self.room = room
        self.inShop = False
        room.addShop(self)
        if roomChoice != None:
            chooseShop = roomChoice
        else:
            chooseShop = random.randint(0, 4)
        if chooseShop == 0:
            self.name = "Khris' Kitchen"
            self.products = [Consumable("Coffee", "Mmm bean juice! Increases intelligence by 2."), Consumable("Honey Bottle", "#savethebees! Increases strength by 2"), Consumable("Bear Claw", "Disclaimer: a pastry, not a real claw! Restores 10 HenPoints")]
        elif chooseShop == 1:
            self.name = "Chubby Penguin's Cafe"
            self.products = [Consumable("Dried Kelp", "Crispy crunchy snack! Restores 5 HenPoints"), Consumable("Raw Cod", "Too bad you don't know how to cook! Restores 10 HenPoints"), Consumable("Cooked Salmon", "Grilled to perfection! Restores 30 HenPoints")]
        elif chooseShop == 2:
            self.name = "Tam, Tim, Tom, and Tum's Tradeporium"
            self.products = [Weapon("Sharpened Stick", "A weapon... Sorta. It's better than nothing, right?."), Armor("Duck Socks", "You can wear them on your head! Raises armor by 2"), Consumable("Bubble Tea", "Good thing you brought your reusable straw! Restores 5 HenPoints and temporarily raises intelligence and strength")]
        elif chooseShop == 3:
            self.name = "Jam, Jim, and Jom's Jamboree"
            self.products = [Weapon("Pocket Knife", "A weapon. Careful, it's sharp!"), Consumable("Rope"), Consumable("Beef Jerky", "Spicy cracker pepper flavor! Restores 10 HenPoints")]
        elif chooseShop == 4:
            self.name = "Rab's Radioactive Resources"
            self.products = [Weapon("Airplane Shrapnel", "A weapon made from recycled material!"), Armor("Life Vest", "Saves you from a big owie! Must be equipped to work."), Consumable("Irradiated Pretzels")]
        

    def showProducts(self, shop):
        if shop == "Khris' Kitchen":
            print("Coffee - 20 Hubucks, temporarily raises intelligence")
            print("Honey Bottle - 20 Hubucks, temporarily raises strength")
            print("Bear Claw - 18 Hubucks, restores 10 HenPoints")
        elif shop == "Chubby Penguin's Cafe":
            print("Dried Kelp - 10 Hubucks, restores 5 HenPoints")
            print("Raw Cod - 18 Hubucks, restores 10 HenPoints")
            print("Cooked Salmon - 50 Hubucks, restores 30 HenPoints")
        elif shop == "Tam, Tim, Tom, and Tum's Tradeporium":
            print("Sharpened Stick - 30 Hubucks, a weapon used to poke opponents")
            print("Duck Socks - 40 Hubucks, armor +2")
            print("Bubble Tea - 30 Hubucks, restores 5 HenPoints and temporarily raises intelligence and strength")
        elif shop == "Jam, Jim, and Jom's Jamboree":
            print("Pocket Knife - 45 Hubucks, a weapon frequently used by campers")
            print("Rope - 60 Hubucks, used to escape risky situations!")
            print("Beef Jerky - 18 Hubucks, restores 10 HenPoints")
        elif shop == "Rab's Radioactive Resources":
            print("Airplane Shrapnel - 60 Hubucks, a weapon built from plane wreckage")
            print("Life Vest - 100 Hubucks, saves you from one potentially life threatening attack")
            print("Irradiated Pretzels - 50 Hubucks, questionable food with unknown effects")

    def shopInfo(self, player):
        clear()
        self.inShop = True
        print("You are in", str(self.name) + "!")
        while self.inShop == True:
            if self.name == "Tam, Tim, Tom, and Tum's Tradeporium":
                playerChoice = input("Would you like to buy, sell, or leave? ")
                if playerChoice.strip() == "sell":
                    print("\n")
                    print("Things you have:")
                    for i in player.items:
                        print(i.name)
                    print("\n")
                    item = input("What would you like to sell? ")
                    for i in player.items:
                        if str(i.name).lower() == str(item).lower():
                            player.money += i.price
                            player.items.remove(i)
                            print(item, "successfully sold! \n")
                        else:
                            print("You don't seem to have that item. \n")
                elif playerChoice.strip().lower() == "buy":
                    print("\n")
                    self.showProducts(self.name)
                    print("\n")
                    purchase = input("What would you like to buy? ")
                    received = False
                    for prod in self.products:
                        if str(purchase.strip().lower()) == str(prod.name.strip().lower()):
                            if player.money - prod.price < 0:
                                print("It seems you don't have enough Hubucks...")
                                print("\n")
                                received = None
                            else:
                                if player.items == []:
                                    print("\n")
                                    print(str(self.name) + " thanks you for your purchase!")
                                    player.money -= prod.price
                                    print("You now have", player.money, "Hubucks")
                                    print("\n")
                                    received = True
                                    break
                                else:
                                    for item in player.items:
                                        if item.name.strip().lower() == purchase.strip().lower():
                                            print("You are already holding a", item.name)
                                            print("\n")
                                            received = None
                                            break
                                        else:
                                            print("\n")
                                            print(str(self.name) + " thanks you for your purchase!")
                                            player.money -= prod.price
                                            print("You now have", player.money, "Hubucks")
                                            print("\n")
                                            received = True
                                            break
                    if received == False:
                        print("That doesn't seem to be an item in this store!")
                        print("\n")
                    elif received == True:
                        player.items.append(prod)
                elif playerChoice.strip().lower() == "leave":
                    self.inShop = False
                else:
                    self.inShop = False
            else:
                playerChoice = input("Would you like to buy or leave? ")
                if playerChoice.strip().lower() == "buy":
                    print("\n")
                    self.showProducts(self.name)
                    print("\n")
                    purchase = input("What would you like to buy? ")
                    received = False
                    for prod in self.products:
                        if str(purchase.strip().lower()) == str(prod.name.strip().lower()):
                            if player.money - prod.price < 0:
                                print("It seems you don't have enough Hubucks...")
                                print("\n")
                                received = None
                            else:
                                if player.items == []:
                                    print("\n")
                                    print(str(self.name) + " thanks you for your purchase!")
                                    player.money -= prod.price
                                    print("You now have", player.money, "Hubucks")
                                    print("\n")
                                    received = True
                                    break
                                else:
                                    for item in player.items:
                                        if item.name.strip().lower() == purchase.strip().lower():
                                            print("You are already holding a", item.name)
                                            print("\n")
                                            received = None
                                            break
                                        else:
                                            print("\n")
                                            print(str(self.name) + " thanks you for your purchase!")
                                            player.money -= prod.price
                                            print("You now have", player.money, "Hubucks")
                                            print("\n")
                                            received = True
                                            break
                    if received == False:
                        print("That doesn't seem to be an item in this store!")
                        print("\n")
                    elif received == True:
                        player.items.append(prod)
                elif playerChoice.strip().lower() == "leave":
                    self.inShop = False
                else:
                    self.inShop = False
