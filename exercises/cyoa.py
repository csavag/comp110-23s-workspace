"""EX06- Choose your own adventure."""
__author__ = "730552002"
import time 
import random


def main() -> None:
    global points
    points: int = 0
    global player
    player: str = ""


def greet() -> None:
    global player
    print("You are standing in a field covered in silvery grass. A gentle breeze pushes waves through it.")
    time.sleep(5.7)
    print("A dark figure on a dark horse stands before you. Based on his whole aesthetic, you judge that he is a villain.")
    time.sleep(7.5)
    print("He swings a sword at your head, further confirming his status as a villain and whispers to you:")
    time.sleep(5.8)
    print("\"Go back to sleep or die.\"")
    time.sleep(2)
    print("The sword comes down toward your head")
    time.sleep(3)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(3)
    print("You awaken due to being violently shaken.")
    time.sleep(2)
    print("\"Great hero! You have arrived! Please, tell me your name!\"")
    player = input()
    print("You sit up. It seems you have fallen from the sky and crashed through the roof of an old man's home. That's somewhat unusual.")
    time.sleep(8)
    print(f"\"Oh great {player}, will you defeat the bad guy and save us?\"")


def choice_1() -> None:
    choice = ""
    while choice != "1" or choice != "2" or choice != "3":
        print("Will you help the old man (1), kill the old man (2), or go back to sleep (3)?")
        choice = input()
    if choice == "1":
        pass


if __name__ == "__main__":
    main()
    greet()
    choice_1()