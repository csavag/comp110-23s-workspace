"""EX03- Wordle with a semblance of structure."""
__author__ = "730552002"


def contains_char(word: str, letter: str) -> bool:
    """Determines if letter is in word at any index."""
    assert len(letter) == 1
    n: int = 0
    while n < len(word):
        if letter == word[n]:
            return True
        n = n + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of colored boxes for the word."""
    assert len(guess) == len(secret)
    result: str = ""
    n: int = 0
    while n < len(secret):
        if guess[n] == secret[n]:
            result = result + "\U0001F7E9"
        else:
            if contains_char(secret, guess[n]):
                result = result + "\U0001F7E8"
            else:
                result = result + "\U00002B1C"
        n = n + 1
    return result


def input_guess(expected_length: int) -> str:
    """Gets user guess or something."""
    inp: str = input(f"Enter a {expected_length} character word: ")
    while len(inp) != expected_length:
        inp = input(f"That wasn't {expected_length} chars! Try again. ")
    return inp


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    turn: int = 1
    secret_word: str = "codes"
    running = True
    while running:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            running = False
        turn = turn + 1
        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
            running = False
    

if __name__ == "__main__":
    main()