"""Choose Your Own Adventure Random Number Guesser."""
__author__ = "730573460"


from random import randint


DOWN_ARROW: str = "\U00002B07"
UP_ARROW: str = "\U00002B06"
TROPHY: str = "\U0001F3C6"
SAD_FACE: str = "\U0001F625"
points: int = 0
player: str = ""
turn: int = 1
round_number: int = 0
secret: int = randint(1, 50)


def main() -> None:
    """Main function that enters and controls game loop."""
    global points
    global secret
    points = 100
    global player
    greet()
    mode: int = int(input(f"You are on round {round_number}. Which mode would you like to enter? Respond with the corresponding number: \n1. Easy mode: higher or lower feedback will be provided \n2. Hard mode: only correct or incorrect feedback is provided \n3. End Adventure \n"))
    while mode < 3:
        secret = randint(1, 50)
        if mode == 1:
            easy_mode()
        if mode == 2:
            points = hard_mode(points)
        mode = int(input(f"You are on round {round_number}. Which mode would you like to enter? Respond with the corresponding number: \n1. Easy mode: higher or lower feedback will be provided \n2. Hard mode: only correct or incorrect feedback is provided \n3. End Adventure \n"))
    if mode == 3:
        print(f"See you next time {player}! You ended on round {round_number} and got {points} points.")


def greet() -> None:
    """Greets players at begining and gives instructions."""
    global player
    player = input("What is your name? ")
    print(f"Hello, {player}! \nIn this game, the goal is to guess a secret number between 1 and 50. \nYou start with 100 points.  \nGamble how many points to add or subtract to your score if you can guess within 10 turns! \nThe more points earned, the better!")


def easy_mode() -> None:
    """Game with higher or lower feedback give."""
    global points
    global round_number
    global player
    print(f"You currently have {points} points.")
    gamble: int = int(input("How many points would you like to gamble? "))
    turn: int = 1
    win: bool = False
    while turn <= 10 and win is False:
        print(f"Turn {turn}/10")
        guess: int = int(input("Guess a random number 1 - 50. "))
        while guess > 50 or guess < 1:
            print("Guess out of range. Try again")
            guess = int(input("Guess a random number 1 - 50. "))
        if guess > secret:
            print(f"{player}, your guess is too high! Try a lower number {DOWN_ARROW}")
        if guess < secret:
            print(f"{player}, your guess is too low! Try a higher number {UP_ARROW}")
        if guess == secret:
            print(f"Great job! You guessed the secret number in {turn} turns! {TROPHY}")
            win = True
        if turn == 10 and win is False:
            print(f"{player}, you lost {gamble} points.")
        turn += 1
    if win is True:
        points += gamble
    if win is False:
        points -= gamble
    round_number += 1
    

def hard_mode(a: int) -> int:
    """Hard game with only correct or incorrect feedback given."""
    global round_number
    new_points: int = a
    print(f"You currently have {new_points} points.")
    gamble: int = int(input("How many points would you like to gamble? "))
    turn: int = 1
    win: bool = False
    guess: int = int(input("Guess a random number 1 - 50."))
    while turn < 10 and win is False:
        while guess > 50 or guess < 1:
            print("Guess out of range. Try again")
            guess = int(input("Guess a random number 1 - 50. "))
        if guess != secret:
            print(f"{player}, your guess is incorrect {SAD_FACE}")
            turn += 1
            print(f"Turn {turn}/10")
            guess = int(input("Guess a random number 1 - 50. "))
        if guess == secret:
            print(f"Great job! You guessed the secret number in {turn} turns! {TROPHY}")
            win = True
    if win is True:
        new_points += gamble
    if win is False:
        new_points -= gamble
    round_number += 1
    return new_points
    

if __name__ == "__main__":
    main()