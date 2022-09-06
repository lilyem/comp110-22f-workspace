"""One shot Wordle."""
__author__ = "730573460"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_of_guess: int = 0
resulting_emojis: str = ""

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

match_in_word: bool = False
alternate_index: int = 0
# The while loop below goes through each index of the guess to see
# if it matches the index in the secret word, matches a different
# index in the secret word, or is not present in the secret word
# at all and prints a different color box for each result
while index_of_guess < len(secret_word):
    if guess[index_of_guess] == secret_word[index_of_guess]:
        resulting_emojis = resulting_emojis + GREEN_BOX
    else:
        while match_in_word != True and alternate_index < len(secret_word):
            if secret_word[alternate_index] == guess[index_of_guess]:
                match_in_word = True
            else: 
                alternate_index = alternate_index + 1
        if match_in_word == True:
            resulting_emojis = resulting_emojis + YELLOW_BOX
        else:
            resulting_emojis = resulting_emojis + WHITE_BOX
    index_of_guess = index_of_guess + 1
    # reset the variables
    match_in_word = False
    alternate_index = 0
print(resulting_emojis)

while len(guess) == len(secret_word):
    if guess == secret_word:
       print("Woo! You got it!")
       quit()
    else:
        print("Not quite. Play again soon!")
        quit()