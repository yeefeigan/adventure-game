# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(item, enemy):
    print_pause("You find yourself standing in an open field, filled "
                "with grass, and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def adventure_choice(item, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2).\n")
        if choice == "1":
            house(item, enemy)
            break
        elif choice == "2":
            cave(item, enemy)
            break
        else:
            print_pause("Sorry, I don't understand.")


def house(item, enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                "steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    if "sword" not in item:
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")
    while True:
        action = input("Would you like to (1) fight or (2) run away?")
        if action == "1":
            fight(item, enemy)
            break
        if action == "2":
            run(item, enemy)
            break
        else:
            print_pause("Sorry, I don't understand.")


def cave(item, enemy):
    print_pause("You peer cautiously into the cave.")
    if "sword" in item:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        item.append("sword")
    print_pause("You walk back out to the field.\n")
    adventure_choice(item, enemy)


def fight(item, enemy):
    if "sword" in item:
        print_pause("As the " + enemy + " moves to attack, you unsheath "
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny "
                    "new toy and runs away!")
        print_pause("You have rid the town of the "+enemy+". "
                    "You are victorious!\n")
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + enemy + ".")
        print_pause("You have been defeated!\n")
    play_again()


def run(item, enemy):
    print_pause("You run back into the field. Luckily, you don't seem to have "
                "been followed.\n")
    adventure_choice(item, enemy)


def play_again():
    response = input("Would you like to play again? (y/n)").lower()
    if response == "y":
        print_pause("Excellent! Restarting the game ...\n")
        play_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.\n")
    else:
        play_again()


def play_game():
    item = []
    enemy = random.choice(["pirate", "goblin", "dragon", "troll", "giants"])
    intro(item, enemy)
    adventure_choice(item, enemy)


play_game()
