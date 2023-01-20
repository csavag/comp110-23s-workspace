import random
import pathlib
global board
global word
global below
global count
def wordcheck(gues):
    n = 0
    correct_letters = 0
    for space in board:
        board[n] = ("|" + gues[n] + "|")
        if word[n] == gues[n]:
            below[n] = ("o")
            correct_letters += 1
        else:
            if gues[n] in word:
                below[n] = ("/")
            else:
                below[n] = ("x")
        n += 1
    stt = ""
    for item in below:
        stt += item
    print(stt)
    print("Tries: " + str(count) + "/6")
    if correct_letters == 5:
        print("Congratulations! You solved the Wordle in " + str(count) + " tries!")
        exit()
words = (open("words.txt", "r"))
lst = words.read().split("\n")
board = ["|_|"] * 5
below = ["x"] * 5
count = 1
#here
word = lst[random.randint(0,495)]
while count < 7:
    print("Input a five-letter word")
    guess = input().lower()
    while len(guess) != 5:
        print("Five letters. Try again.")
        guess = input().lower()
    wordcheck(guess)
    count += 1
print("You did not solve the Wordle. The correct word was " + word + ".")