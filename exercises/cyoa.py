"""EX06- Choose your own adventure."""
__author__ = "730552002"
import time 
import random
import sys
global points
points: int = 0
global player
player: str = ""
global playing
playing: bool = True


def main() -> None:
    greet()
    #global points
    #global player
    #points: int = 0
    #player: str = ""


def read_time(sentence):
    print(sentence)
    lstt = sentence.split()
    time_count = 0
    for item in lstt:
        if len(item) > 3:
            time_count += 1
        else:
            time_count += 0.3
    while time_count < (len(lstt) - 4):
        time_count += 1
    if time_count < 2:
        time_count += 1.5
    time.sleep(time_count/3)


def greet() -> None:
    global player
    print("~~~ Chapter One ~~~")
    time.sleep(3)
    read_time("You are standing in a field covered in silvery grass. A gentle breeze pushes waves through it.")
    read_time("A dark figure stands before you. Based on his whole aesthetic, you judge that he is a villain.")
    read_time("He swings a sword at your head, further confirming his status as a villain and whispers to you:")
    read_time("\"Go back to sleep or die.\"")
    time.sleep(1)
    read_time("The sword comes down toward your head.")
    print(".")
    time.sleep(1.5)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2.5)
    read_time("You awaken due to being violently shaken.")
    print("\"Great hero! You have arrived! Please, what is your name!\"(Input)")
    player = input()
    read_time("You lift your head. It seems you have fallen from the sky and crashed through the roof of an old man's home. That's somewhat unusual.")
    read_time(f"\"Oh great {player}, will you defeat the bad guy and save us?\"")


def choice_1() -> None:
    choice = ""
    global points
    global player
    while choice != "1" and choice != "2" and choice != "3":
        print("Will you help the old man (1), kill the old man (2), or go back to sleep (3)?")
        choice = input()
    if choice == "3":
        read_time("You choose to lay your head down and go back to sleep.")
        read_time("\"What? No! You must save us!\"")
        read_time("But you just went to sleep.")
        print("You did not save anything.")
        sys.exit(f"You scored {points} points, {player}.")
    if choice == "1":
        points += 1
        read_time("You stand up with great vigor.")
        read_time("\"Oh jolly good! Come, I'll show you the way.")
        read_time("The old man picks you up and takes you outside.")
        read_time("He lifts you above his head and shouts:")
        time.sleep(1)
        read_time("\"Everyone! I have found our hero!\"")
        read_time("Nearby village people look over, confused and concerned.")
        read_time("One person calls out:")
        time.sleep(1)
        read_time("\"Shut it, old man! You're always going on about some nonsense. Put that thing down and go work the field.\"")
        read_time("You look at the person and quack.")
        time.sleep(1)
        read_time("Because you are a duck.")
        time.sleep(1)
        read_time("The old man replies:")
        read_time("\"This is our hero of prophecy!\"")
        time.sleep(1)
        read_time("The person calls out again:")
        time.sleep(1)
        read_time("\"There is no prophecy! That duck fell out of a flock as they passed over your house.\"")
        time.sleep(1.5)
        read_time("The old man waves them off.")
        read_time("\"Bah! This is our hero. They will save us.\"")
        read_time(f"\"The bad guy is that way, {player}. Have at him!\"")
        read_time("And with that, the old man throws you in the direction he indicated.")
        read_time("You fly in that direction, off to save everyone and everything from the bad guy.")
        print("End of chapter one. Press enter to continue.")
        input()
    if choice == "2":
        points -= 1
        read_time("You glare at the old man.")
        read_time("He stumbles back, horrified by the malice in your gaze.")
        read_time("\"You... you are no hero. You are an evil duck!\"")
        read_time("You rise to your full height, lift your wings, and quack mencaingly at the old man.")
        read_time("He screams in horror as you descend on him, ripping and tearing flesh.")
        time.sleep(2)
        read_time("You step out of the old man's house, meeting villagers with your icy stare.")
        read_time("They cower at your might and bloodstained feathers.")
        read_time("Now, you must find that being that spoke to you in your dream. Nobody threatens you and gets away with it.")
        read_time("You sense evil in the air and fly toward it, knowing that it will take you to the dark one.")
        print("End of chapter one. Press enter to continue.")
        input()


def choice_2() -> None:
    global points
    print("~~~ Chapter Two ~~~")
    time.sleep(3)
    read_time("As you fly toward the bad guy, you spy a young child feeding ducks in a pond.")
    choice = ""
    while choice != "1" and choice != "2" and choice != "3":
        print("Will you say hi to the ducks (1), attack the child (2), or pass them by (3)?")
        choice = input()
    if choice == "3":
        read_time("You keep flying toward the bad guy.")
    if choice == "1":
        points += 1
        read_time("You swoop down and land next to the child.")
        read_time("You quack at the ducks.")
        time.sleep(1)
        read_time("They quack back.")
        time.sleep(1)
        read_time("All is well here.")
        time.sleep(2)
        read_time("The child speaks to you.")
        read_time("\"Hello there, little duck. Would you like a bread?\"")
        read_time("The child hands you a slice of bread.")
        read_time("You got a bread!")
        time.sleep(1.5)
        if points > 0:
            read_time("However, since you are on a gluten-free diet, you can't eat it.")
            read_time("Despite that, you have good manners, so you quack gratefully at the child.")
            read_time("Holding the bread, you take off and fly onward toward the bad guy.")
        else:
            read_time("You swallow the bread whole.")
            read_time("The child is holding another piece of bread to feed to the other ducks.")
            read_time("You snatch it along with the child's thumb.")
            read_time("The child falls back as you eat both the bread and the thumb.")
            read_time("You fly onward toward the enemy that threatened you.")
    if choice == "2":
        points -= 1
        read_time("You dive toward the child and knock them over.")
        if points > -1:
            read_time("The child screams as you scratch and bite at them, mutilating them horribly.")
        else:
            read_time("The child screams as you tear them limb from limb, slurping down juicy pieces of meat.")
        read_time("You eat the loaf of bread the child brought to feed the ducks in the pond.")
        read_time("You fly onward toward the bad guy.")
    print("End of chapter two. Press enter to continue.")
    input()


def choice_3(point_count, name) -> int:
    print("~~~ Chapter Three ~~~")
    time.sleep(3)
    read_time("After a lengthy flight, you find a wide field covered in silvery grass.")
    read_time("It is the field from your dream.")
    read_time("A dark figure stands in the middle, watching as you land in front of him.")
    read_time("You can't see his face beneath his black hood, but he speaks to you in a cold voice.")
    read_time(f"\"You have come, {name}. Fine, then. I will destroy everyone and everything, starting with you.\"")
    read_time("\"It's duck season!\"")
    time.sleep(1)
    read_time("You want to tell him that it's rabbit season, but you can only quack.")
    read_time("The final confrontation is upon you. What will you do?")
    choice = ""
    while choice != "1" and choice != "2" and choice != "3":
        if point_count == 2:
            print("Reason with the figure (1), attack the figure (2), join forces with the figure (3), offer the bread (4)")
        else:
            print("Reason with the figure (1), attack the figure (2), join forces with the figure (3).")
        choice = input()
        if choice == "1":
            read_time("You try to reason with the figure.")
            read_time("But he won't listen.")
            choice = ""
        if choice == "4" and point_count == 2:
            point_count += 1
            read_time("You drop your bread on the floor.")
            read_time("The bad guy sees the bread and leaps toward it with great speed.")
            read_time("In his haste, his hood flies off to reveal-")
            read_time("A duck.")
            read_time("He gobbles up the bread and cries out:")
            read_time("\"No! Now you know who I really am. Yes, I am a duck, like you.\"")
            read_time("He casts aside his cloak. Beneath it lies a massive, absolutely ripped human body. Muscles abound.")
            read_time("You did not know muscles could get that big.")
            read_time("\"You may be wondering why I'm going to destroy everything. It's because I am angry!\"")
            read_time("\"I was so lazily written! Look at me! How could a being like me exist? It is shameful!\"")
            read_time("\"Every day I curse the thing known only as 730552002, the monster that created me.\"")
            read_time("\"Now you know my story. And... it feels good to speak it aloud.\"")
            read_time("He lets out a sigh.")
            read_time("\"I... I don't want to do this anymore. Perhaps with a therapist like you, I don't need to destroy everything.\"")
            read_time("He sits down. You place a wing on his shoulder. Everything is ok now.")
            time.sleep(2)
            print("You saved everything without conflict. Good job!")
            return point_count
        if choice == "2":
            read_time("You fly at the figure's head.")
            read_time("But he grabs you out of the air and kneels on your chest.")
            read_time("\"You are but a simple duck, fool. You cannot fight me.\"")
            point_count += 1
            effort = 0
            while effort < 2:
                read_time("The bad guy is choking you. It's life or death. What will you do?")
                choice_sub = ""
                while choice_sub != "1" and choice_sub != "2":
                    print("Struggle (1) or die (2)")
                    choice_sub = input()
                    if choice_sub == "1":
                        effort += 1
                        if effort < 3:
                            read_time("You struggle and squirm, trying to get out, but you can't quite make it.")
                            read_time("You don't want to die here. What will you do?")
                    if choice_sub == "2":
                        read_time("Your movements slow down. Your vision fades.")
                        time.sleep(1)
                        read_time("The bad guy was too strong.")
                        time.sleep(2)
                        read_time("You die.")
                        time.sleep(2)
                        print("You made a valiant effort, but did not save anything.")
                        return point_count
            read_time("You fight with all your strength and feel the bad guy lift up a little bit.")
            read_time("But he snarls and comes crashing back down on you.")
            point_count += 1
            print("What will you do?")
            print("Fight! (1) or fight! (2)")
            input()
            read_time("With a quack of strength and defiance, you throw the bad guy off you.")
            read_time("He sails twenty feet before crashing back to the ground.")
            if point_count > 2:
                read_time("You can defeat him.")
                read_time("You are the hero.")
            else:
                read_time("This wretch is nothing to you.")
                read_time("You are stronger than him.")
            read_time("As he stumbles to his feet, you flap to your feet and build up your strength.")
            read_time("Your body thrums with power.")
            read_time("The bad guy lets out a yell and charges at you.")
            read_time("You let out your own quack and expel pure energy from your mouth in the form of a blindingly bright beam.")
            read_time("The beam of energy strikes him.")
            read_time("He screams in awe of your power and disintegrates into nothing.")
            time.sleep(2)
            read_time("The battle is over. You won.")
            time.sleep(2)
            print("You saved everything. Well done!")
            return point_count
        if choice == "3":
            read_time("You offer to join forces with the bad guy.")
            read_time("\"You would join me? The great hero?\"")
            read_time("Surprised, he accepts.")
            time.sleep(1)
            read_time("Together, you destroy everyone and everything.")
            read_time("Unfortunately, that includes you and the bad guy.")
            read_time("You both die.")
            time.sleep(1)
            print("You destroyed everyone and everything. Shame on you.")
            return point_count


if __name__ == "__main__":
    while playing:
        main()
        choice_1()
        choice_2()
        print(f"You scored {choice_3(points, player)} points, {player}.")
        again = ""
        while again != "1" and again != "2":
            print("Do you want to play again? Yes (1) or no (2).")
            again = input()
            if again == "2":
                playing = False
                print("Thank you for playing.")