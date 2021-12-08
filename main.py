from room import Room
from player import Player
from player import Henry
from player import Hubert
from item import Item
from item import Weapon
from item import Armor
from item import Consumable
from monster import Monster
from shop import Shop
from npc import Npc
import os
import updater

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def titleScreen():
    clear()
    print("  _    _                                              _   _    _         _                 _   _ ")
    print(" | |  | |                                            | | | |  | |       | |               | | ( )")
    print(" | |__| |  ___  _ __   _ __  _   _    __ _  _ __   __| | | |__| | _   _ | |__   ___  _ __ | |_|/ ___")
    print(" |  __  | / _ \| '_ \ | '__|| | | |  / _` || '_ \ / _` | |  __  || | | || '_ \ / _ \| '__|| __| / __|")
    print(" | |  | | | __/| | | || |   | |_| |  |(_| || | | ||(_| | | |  | || |_| || |_) || __/| |   | |_  \__ \ ")
    print(" |_|  |_| \___||_| |_||_|    \__, |  \__,_||_| |_|\__,_| |_|  |_| \__,_||_.__/ \___||_|    \__| |___/")
    print("                              __/ |")
    print("                             |___/")
    print(" _______           _                  _                     _                       ___    ____")
    print("|__   __|         | |       /\       | |                   | |                     |__  \ /  _  \ ")
    print("   | |  ___ __  __| |_     /  \    __| |__   __ ___  _ __  | |_  _   _  _ __  ___     )  || | | |")
    print("   | | / _ \\\\ \/ /| __|   / /\ \  / _` |\ \ / // _ \| '_ \ | __|| | | || '__|/ _ \   /  / | | | |")
    print("   | | | __/ >  < | |_   / ____ \ |(_| | \ V /|  __/| | | || |_ | |_| || |   | __/  /  /_ | | | |")
    print("   |_| \___|/_/\_\ \__| /_/    \_\\\\__,_|  \_/  \___||_| |_| \__| \__,_||_|   \___| |____(_)____/", "\n")
    print("   ________         ____/___")
    print(" /   *   *  \     /   *   *  \ ")
    print("|    { * }   |   |    { * }   |")
    print("|     / \    |   |     / \    |")
    print(" \ ________ /     \ ________ /")
    print("   ()    ()         ()    ()", "\n")
    input("Press enter to start")
titleScreen()

player = None
def playerSelect():
    clear()
    print("Welcome to the new and improved version of Henry and Hubert's Text Adventure! \n")
    print("Twins Henry and Hubert have both made it back home in San Jose. What could go wrong?")
    print("Well it turns out, they have some new siblings! On top of that, the house is a mess.")
    print("It looks like they'll be doing loads of clean up! \n")
    print("Choose a character:")
    print("Henry: Raised by a human since birth, better at talking it through than fighting (strength: 6, intelligence: 4) \n")
    print("Hubert: Neglected as a cub, learned to fend for himself but isn't the brightest (strength: 8, intelligence: 2) \n")
    global player
    while player == None:
        choice = input("Henry or Hubert? ")
        selection = choice.strip()
        if selection == "Henry" or selection == "henry":
            player = Henry()
            print("\nGreat choice! Here's some information on Henry:")
            print("- An international superspy.")
            print("- Acts like a potato. Specifically a Yukon Gold.")
            print("- Likes cooking in his free time.")
            print("- A big fan of dinosaurs \n")
        elif selection == "Hubert" or selection == "hubert":
            player = Hubert()
            print("\nGreat choice! Here's some information on Hubert:")
            print("- An adventurous ninja.")
            print("- Believes he is a loaf of bread, waiting to become a crouton.")
            print("- Avid Hot Wheel collector.")
            print("- Really likes insects. \n")
        else:
            print("That is not an option, try again!")
    return player
playerSelect()

def createWorld():
    mapCheck = False
    while mapCheck == False:
        mapSelect = input("Now, which house are you going to, Lock or Key? ")
        if mapSelect.strip().lower() == "lock":
            bedroom = Room("You are in Lock's bedroom")
            hallway = Room("You are in the hallway")
            grandparents = Room("You are in grandparent's room")
            auntie = Room("You are in auntie's room")
            livingroom = Room("You are in the living room")
            kitchen = Room("You are in the kitchen")
            den = Room("You are in the den")
            storage = Room("You are in the storage")
            garden = Room("You are in the garden")
            porch = Room("You are on the porch")
            Room.connectRooms(bedroom, "north", hallway, "south")
            Room.connectRooms(hallway, "north", livingroom, "south")
            Room.connectRooms(hallway, "east", auntie, "west")
            Room.connectRooms(hallway, "west", grandparents, "east")
            Room.connectRooms(livingroom, "north", kitchen, "south")
            Room.connectRooms(livingroom, "east", den, "west")
            Room.connectRooms(livingroom, "west", garden, "east")
            Room.connectRooms(kitchen, "north", storage, "south")
            Room.connectRooms(storage, "east", porch, "west")
            Room.connectRooms(porch, "south", den, "north")
            box = Armor("Cardboard Box", "Super stealthy. You're just like Snake!")
            box.putInRoom(storage)
            Monster("Germ Cluster", hallway)
            mapCheck = True
        elif mapSelect.strip().lower() == "key":
            bedroom = Room("You are in Key's bedroom")
            hallway1 = Room("You are in the first part of the hallway")
            hallway2 = Room("You are in the second part of the hallway")
            hallway3 = Room("You are in the third part of the hallway")
            grandparents = Room("You are in grandparent's room")
            auntie = Room("You are in auntie's room")
            guestroom = Room("You are in the guest room")
            musicroom = Room("You are in the music room")
            garden = Room("You are in the garden")
            kitchen = Room("You are in the kitchen")
            livingroom = Room("You are in the living room")
            porch = Room("You are on the porch")
            Room.connectRooms(bedroom, "north", hallway1, "south")
            Room.connectRooms(hallway1, "north", auntie, "south")
            Room.connectRooms(hallway1, "east", hallway2, "west")
            Room.connectRooms(hallway1, "west", grandparents, "east")
            Room.connectRooms(hallway2, "north", guestroom, "south")
            Room.connectRooms(hallway2, "east", hallway3, "west")
            Room.connectRooms(hallway2, "south", musicroom, "north")
            Room.connectRooms(musicroom, "south", kitchen, "north")
            Room.connectRooms(musicroom, "west", garden, "east")
            Room.connectRooms(kitchen, "east", livingroom, "west")
            Room.connectRooms(livingroom, "north", hallway3, "south")
            Room.connectRooms(hallway3, "east", porch, "west")
            Monster("Germ Cluster", hallway1)
            mapCheck = True
        else:
            print("That's not an option! Try again please. ")
    player.location = bedroom
    if player.character == "Henry":
        Npc("Hubert", bedroom)
    else:
        Npc("Henry", bedroom)
    Monster("Vacuum Bag", grandparents)
    Monster("Grease Jar", porch)
    Monster("Coffee Cup", auntie)
    Monster("Plastic Knife", garden)
    Monster("Dishwasher", kitchen)
    Monster("Stained Couch", livingroom)
    Monster.spawnMonster(player.location)
    Shop(kitchen, 0)
    print("\nCool, see you in there!")
    input("Press enter to continue ")

def printSituation():
    clear()
    print(player.location.desc)
    print()
    print("Type \"help\" for help!")
    print()
    if player.location.hasNpc():
        for n in player.location.npc:
            print("You can talk to " + str(n.name) + "!")
        print()
    if player.location.hasShop():
        for s in player.location.shop:
            print(s.name, "is in this room!")
        print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("The goal of the game is to clean up the house.")
    print("You'll want to defeat dirt monsters. The big ones will give you quarters.")
    print("Once you have enough quarters, talk to your brother in the bedroom.")
    print("You can also talk to him now for more help! \n")
    print("Here's some commands you can do: ")
    print("me -- shows your health and current stats")
    print("inventory -- opens your inventory")
    print("inspect <item> -- displays information on the specified items")
    print("wait -- allows time to pass without moving locations (possible monster spawns, status boosts deplete)")
    print("go <north/east/south/west> -- moves you in the given direction.")
    print("pickup <item> -- picks up the item")
    print("equip <item> -- equips the specified item")
    print("eat <item> -- allows you to eat a food item")
    print("drop <item> -- drops the item back to the ground")
    print("delete <item> -- destroys the item from your inventory")
    print("clean <monster> -- cleans the specified monster")
    print("visit -- allows you to visit the shop in a location if there is one")
    print("talk -- opens up a chat menu with your brother if he's in the same place as you!")
    print("exit -- quits the game")
    print()
    input("Press enter to continue...")

createWorld()
playing = True
while playing and player.alive and not player.win:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What would you like to do? ")
        commandWords = command.split()
        if command == "":
            print("No command given!")
            commandSuccess = False
        elif commandWords[0].lower() == "go":   #cannot handle multi-word directions
            player.location.checkMonsters(player)
            targetName = command[3:]
            prevLocation = player.location
            roomCount = 0
            for e in player.location.exitNames():
                if str(e).strip() == str(targetName).strip():
                    player.goDirection(commandWords[1])
                    timePasses = True
                else:
                    roomCount += 1
            if roomCount >= len(prevLocation.exitNames()):
                print("That is not a valid direction.")
                commandSuccess = False
        elif commandWords[0].lower() == "wait":
            timePasses = True
            input("Time has passed... Press enter to continue!")
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            adjusted = targetName.strip().lower()
            target = player.location.getItemByName(adjusted)
            if target != False:
                if target.name == "quarter":
                    player.pickup(target)
                else:
                    for item in player.items:
                        if item.name == target.name:
                            print("You are already holding a", target.name)
                            commandSuccess = False
                    player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "inventory":
            player.showInventory()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "clean":
            targetName = command[6:]
            adjusted = targetName.strip().lower()
            target = player.location.getMonsterByName(adjusted)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == "me":
            player.showStats()
            commandSuccess = False
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            targetInv = player.getItemByName(targetName)
            targetGro = player.location.getItemByName(targetName)
            if targetInv != False:
                targetInv.describe()
            elif targetGro != False:
                targetGro.describe()
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "equip":
            targetName = command[6:]
            target = player.getItemByName(targetName)
            if target != False:
                if target.type == "Consumable":
                    print("That item is not equippable")
                    commandSuccess = False
                else:
                    for item in player.items:
                        if item.name == target.name:
                            item.equip(player)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "dequip":
            targetName = command[7:]
            target = player.getItemByName(targetName)
            if target != False:
                for item in player.equipment:
                    if item.name == target.name:
                        item.dequip(player)
            else:
                print("That item is not equipped.")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":
            targetName = command[5:]
            target = player.getItemByName(targetName)
            if target != False:
                for item in player.items:
                    if item.name == target.name:
                        item.putInRoom(player.location)
                        player.items.remove(item)
                for item in player.equipment:
                    if item.name == target.name:
                        player.equipment.remove(item)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "delete":
            targetName = command[7:]
            target = player.getItemByName(targetName)
            if target != False:
                for item in player.items:
                    if item.name == target.name:
                        player.items.remove(item)
                for item in player.equipment:
                    if item.name == target.name:
                        player.equipment.remove(item)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "eat":
            targetName = command[4:]
            target = player.getItemByName(targetName)
            if target != False and target.type == "Consumable":
                for item in player.items:
                    if item.name == target.name:
                        item.eat(player)
                        player.items.remove(item)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "visit":
            if player.location.hasShop():
                Shop.shopInfo(player.location.shop[0], player)
            else:
                print("There is no shop here.")
                commandSuccess = False
        elif commandWords[0].lower() == "talk":
            if player.location.desc == "You are in Lock's bedroom" or player.location.desc == "You are in Key's bedroom":
                if player.npcVisits == 0:
                    player.npcVisits += 1
                    Npc.firstChat(player)
                else:
                    player.npcVisits += 1
                    Npc.chat(player)
            else:
                if player.character == "Henry":
                    name = "Hubert"
                else:
                    name = "Henry"
                print("It doesn't seem like", name, "is here.")
                commandSuccess = False
        else:
            print("Not a valid command")
            commandSuccess = False
        print("\n")
    if timePasses == True:
        Monster.spawnMonster(player.location)
        for item in player.effects:
            item.durability -= 1
            if item.durability <= 0:
                item.removeEffects(player)
                player.effects.remove(item)
        updater.updateAll()

clear()
print()
print("Thanks for playing Henry and Hubert's Text Based Adventure!")
print("Henry and Hubert appreciate the time they've spent with you.")
input("Press enter to say bye! ")
print()
