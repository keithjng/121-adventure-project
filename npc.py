import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Npc:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        room.addNpc(self)
    def firstChat(player):
        # Have NPC heal character by 30 the first time they chat
        clear()
        print("Hey " + str(player.character) + "!" )
        print("Are you hungy? Here, eat some Cooked Salmon. It'll heal you lots!")
        player.health += 30
        player.health = min(100, player.health)
        print("Delicious, right? You can buy more from the cafe later! (Press enter to continue)")
        quarterCount = 0
        for item in player.items:
            if item.name == "Quarter":
                quarterCount += 1
        if quarterCount >= 7:
            player.win = True
        if player.win == True:
            # Game ends, show graphic
            pass
        else:
            Npc.conversation()
    def chat(player):
        clear()
        print("Hey " + str(player.character) + "!" )
        quarterCount = 0
        for item in player.items:
            if item.name == "Quarter":
                quarterCount += 1
        if quarterCount >= 7:
            player.win = True
        if player.win == True:
            # Game ends, show graphic
            pass
        else:
            Npc.conversation()
    def conversation():
        talking = True
        while talking == True:
            input("")
            greeting = input("Do you need some help? ")
            if greeting.strip().lower() == "yes" or greeting.strip().lower() == "y":
                help = True
                while help == True:
                    print()
                    print("What would you like to know about?")
                    print("- Objective")
                    print("- Combat")
                    print("- Monsters")
                    print("- Credits")
                    print()
                    choice = input("Type any of the words above or \"bye\" to leave! ")
                    if choice.strip().lower() == "bye":
                        print()
                        print("See you later! Rada rada rada!")
                        print()
                        input("Press enter to leave the conversation.")
                        help = False
                        talking = False
                    elif choice.strip().lower() == "objective":
                        clear()
                        print("The goal of the game is to clean the house! You'll be going throughout the house, fighting dirt monsters.")
                        print("After you defeat a certain amount of monsters, a boss will spawn! Each boss is holding a quarter.")
                        print("Once you get $1.75, we'll have enough money to pay for the washing machine. Come back and talk to me once you get there!")
                        print("There are a few ways to lose. You'll faint if you run out of HenPoints, meaning you'll have to start from the beginning.")
                        print("You can also lose if you try to leave a room with more than 5 monsters, because the room will be too messy!")
                        input("You can ask me more about fighting and monsters! (Press enter) ")
                    elif choice.strip().lower() == "combat":
                        clear()
                        print("Combat here is pretty simple. You have health you lose when you fight. The damage you take can be reduced with armor.")
                        print("Your strength determines how much you attack with. You can boost these with food and weapons!")
                        print("The other stat used in combat is intelligence. This is your ability to dodge an opponents attacks.")
                        print("Watch out for the bosses, they tend to mess with your stats. Be prepared!")
                        input("You can ask me more about the monsters or how to win this game. (Press enter) ")
                    elif choice.strip().lower() == "monsters":
                        clear()
                        print("There are 7 minion monsters that roam all the rooms! Killing them gives you Hubucks, money you can use at shops!")
                        print("Slaying enough of these will cause certain bosses to spawn in each of the rooms: ")
                        print("- Germ Cluster (in the hallway)")
                        print("- Vacuum Bag (in the grandparents room)")
                        print("- Grease Jar (on the porch)")
                        print("- Coffee Cup (in the aunt's room)")
                        print("- Plastic Knife (in the garden)")
                        print("- Dishwasher (in the kitchen)")
                        print("- Stained Couch (in the living room)")
                        print("These bosses are carrying quarters which we need to collect to do laundry!")
                        input("If you need more clarification on how to get home or how fighting works, just ask! (Press enter) ")
                    elif choice.strip().lower() == "credits":
                        clear()
                        print("This game was made by Keith Ng for a project in Reed College's CSCI 121 class")
                        input("Keith would like to give a huge thanks to Adam Groce and David Ramirez for teaching him how to code in snake! (Press enter) ")
                        print("Uh... Was it snake? I don't remember...")
                        input("How awkward... (Press enter) ")
                    else:
                        input("Huh?? I don't understand, sorry. (Press enter) ")
            elif greeting.strip().lower() == "no":
                print()
                print("See you later! Rada rada rada!")
                print()
                input("Press enter to leave the conversation.")
                talking = False
            else:
                print()
                print("Hmph! It's just a yes or no question! Let's try again.")
                print()
                input("Press enter to continue")
                print()
