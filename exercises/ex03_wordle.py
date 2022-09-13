"""EX03 Structured Wordle."""
__author__ = "730573460"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char (guess: str, character: str) -> bool:
    """Checks if the guess contains characters in secret."""
    assert len(character) ==1
    index_of_guess: int = 0
    while index_of_guess < len(guess):
        if guess[index_of_guess] == character:
            return True
        else:
            index_of_guess = index_of_guess + 1
    return False

def emojified (guess: str, secret: str) -> str:
    """Returns str for emoji color."""
    assert len(guess) == len (secret)
    index_of_guess: int = 0
    resulting_emojis: str = ""
    while index_of_guess < len(guess):
        if guess[index_of_guess] == secret [index_of_guess]:
            resulting_emojis = resulting_emojis + GREEN_BOX
        elif contains_char(secret, guess[index_of_guess]) == True:
            resulting_emojis = resulting_emojis + YELLOW_BOX
        elif contains_char(secret, guess[index_of_guess]) == False:
            resulting_emojis = resulting_emojis + WHITE_BOX
        index_of_guess = index_of_guess + 1
    return resulting_emojis
# The function emojified results in the appropriate emojis when the 
# guess and secret are put as the arguments. If a green box is not concatenated,
# contains_char is called in order to determine if a yellow or while box should 
# be concatenated.

def input_guess (number: int) -> str:
    """Ensures guess is of expected length."""
    guess_input: str = input(f"Enter a {number} character word: ")
    while number != len(guess_input):
        guess_input = input(f"That wasn't {number} chars! Try again: ")
    return guess_input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    game_turn: int = 1
    won: bool = False
    current_guess: str = ""
    while game_turn <= 6 and won == False:
        print(f"=== Turn {game_turn}/6 ===")
        current_guess = input_guess(len(secret))
        print(emojified(current_guess, secret))
        if current_guess == secret:
            won = True
        else:
            game_turn = game_turn + 1
    if won == True:
        print(f"You won in {game_turn}/6 turns!")
    if won == False:
        print(f"X/6 - Sorry, try again tomorrow!")
# The main function calls on the input_guess function first then the emojified
# function. This function results in the wordle game. Defining contains_char, 
# emojified, and input_guess first made building blocks for the main function
# and made the code for it simpler than if it was written all into one function.

if __name__ == "__main__":
    main()
# This allows Python to run this program as a module and allows other modules
# to import and reuse the functions defined here.
