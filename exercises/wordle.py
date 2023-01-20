import random
import pathlib
words = (open("words.txt", "r"))
lst = words.read().split("\n")
board = ["|_|"] * 5
below = [" x "] * 5
print(board)
print(below)
word = lst[random.randint(0,495)]
print("Input a five-letter word")
guess = input().lower()
while len(guess) != 5:
    print("Five letters. Try again.")
    guess = input().lower()
"""for space in board:
    board[board.index(space)] = ("|" + guess[board.index(space)] + "|")
    if word[board.index(space)] == guess[board.index(space)]:
        below[board.index(space)] = (" o ")
    else:
        if guess[board.index(space)] in word:
            below[board.index(space)] = (" / ")
        else:
            below[board.index(space)] = (" x ")"""
print(board)
print(below)    
print(guess)    