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
    pass
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
    read_time("A dark figure on a dark horse stands before you. Based on his whole aesthetic, you judge that he is a villain.")
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
    while choice != "1" and choice != "2" and choice != "3":
        print("Will you help the old man (1), kill the old man (2), or go back to sleep (3)?")
        choice = input()
    if choice == "3":
        read_time("You choose to lay your head down and go back to sleep.")
        read_time("\"What? No! You must save us!\"")
        read_time("But you just went to sleep.")
        playing = False
        print(f"You scored {points} points.")
        sys.exit("You did not save anything or anyone.")
    if choice == "1":
        read_time("You stand up with great vigor.")
        read_time("\"Oh jolly good! Come, I'll show you the way.")
        read_time("The old man picks you up and takes you outside.")
        read_time("The old man lifts you above his head and shouts:")
        time.sleep(1)
        read_time("\"Everyone! I have found our hero!\"")
        read_time("Nearby village people erupt into cheers.")
        read_time("One person steps forward and calls out-")
        time.sleep(1)
        read_time("\"Hang on, now, this is our hero? How are they going to stop the bad guy? They're all feathery.\"")
        read_time("You look at the person and quack.")
        time.sleep(1)
        read_time("Because you are a duck.")
        time.sleep(1)
        read_time("The person calls out again:")
        read_time("\"I saw them fall out of a flock of ducks as they flew over your house, old man.\"")
        time.sleep(1.5)
        read_time("The old man waves them off.")
        read_time("\"Bah! This is our hero. They will save us.\"")
        read_time(f"\"The bad guy is that way, {player}. Have at him!\"")
        read_time("And with that, the old man throws you in the direction he indicated.")
        read_time("You fly in that direction, off to save everyone and everything from the bad guy.")
        print("End of chapter one. Press enter to continue")
        input()


if __name__ == "__main__":
    while playing:
        main()
        greet()
        choice_1()