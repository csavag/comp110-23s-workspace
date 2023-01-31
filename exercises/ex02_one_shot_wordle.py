"""EX02- Wordle but you only get one try lol."""
__author__ = "730552002"

secret_word: str = "python"
guess: str = ""
guess = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
n: int = 0
result: str = ""
while n < len(secret_word):
    if guess[n] == secret_word[n]:
        result = result + "\U0001F7E9"
    else:
        in_word = False
        letter_where = 0
        while not in_word and letter_where < len(secret_word):
            if secret_word[letter_where] == guess[n]:
                in_word = True
            letter_where += 1
        if in_word:
            result = result + "\U0001F7E8"
        else:
            result = result + "\U00002B1C"
    n = n + 1
print(result)