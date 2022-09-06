"""EX01 - Chardle - A cute step toward Wordle."""
__author__= "730573460"


five_letter_word: str=input("Enter a 5-character word: ")
if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str=input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_letter_word)

match_count: int = 0

if single_character == five_letter_word[0]:
    print(single_character + " found at index 0")
    match_count = match_count + 1

if single_character == five_letter_word[1]:
    print(single_character + " found at index 1")
    match_count = match_count + 1

if single_character == five_letter_word[2]:
    print(single_character + " found at index 2")
    match_count = match_count + 1

if single_character == five_letter_word[3]:
    print(single_character + " found at index 3")
    match_count = match_count + 1

if single_character == five_letter_word[4]:
    print(single_character + " found at index 4")
    match_count = match_count + 1

if match_count == 0:
    print("No instances of " + single_character + " found in " + five_letter_word)
    
if match_count == 1:
    print("1 instance of " + single_character + " found in " + five_letter_word)

if match_count > 1:
    print(str(match_count) + " instances of " + single_character + " found in " + five_letter_word)
