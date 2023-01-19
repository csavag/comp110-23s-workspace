"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730552002"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char: str = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character")
    exit()
count: int = 0
print("Searching for " + char + " in " + word)
if word[0] == char:
    print(char + " found at index 0")
    count = count + 1
if word[1] == char:
    print(char + " found at index 1")
    count = count + 1
if word[2] == char:
    print(char + " found at index 2")
    count = count + 1
if word[3] == char:
    print(char + " found at index 3")
    count = count + 1
if word[4] == char:
    print(char + " found at index 4")
    count = count + 1
if count == 1:
    print(str(count) + " instance of " + char + " found in " + word)
if count > 1:
    print(str(count) + " instances of " + char + " found in " + word)
else:
    print("No instances of " + char + " found in " + word)