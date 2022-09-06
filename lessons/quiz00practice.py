"""quiz practice!"""

x: int=7

print("guess a number 1-10")
guess: int=int(input("what number am I thinking of?"))

if guess == x:
    print("you are correct!")
else:
    print("try again")
    if guess>7:
        print("lower number")
    else:
        print("higher number")
print("thanks for playing!")