# Magi8rand by Dominique Hill

from random import randrange

# Rules of the Magic8Rand Game
print("Welcome to Magic8rand. In this game you will be a Magic 8 ball simulation.")
print("Using questions proved by the user,the computer responds with 4 randomly selected answers:")
print("Yes, No, Perhaps, and Ask Again later")

# User asks a question
user = input("Type in a question")

# import randrange variable
myrandom = randrange(1, 5)
print(myrandom)

# Yes, No Way, Perhaps, Ask Again Later
if myrandom == 1:
    print("Yes")
if myrandom == 2:
    print("No")
if myrandom == 3:
    print("Perhaps")
if myrandom == 1:
    print("Ask Again Later")

# play again variable
playagain = "yes"

# While loop for the game to replay
while playagain == "yes":
    user = input("Type in a question")
    myrandom = randrange(1, 5)
    print(myrandom)
    if myrandom == 1:
        print("Yes")
    if myrandom == 2:
        print("No")
    if myrandom == 3:
        print("Perhaps")
    if myrandom == 4:
        print("Ask Again Later")
    playagain = input("Would you like to play. Enter yes/no")

if playagain != "yes":
    print("Thanks for playing")
    print("End")
