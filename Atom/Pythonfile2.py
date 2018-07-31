number = 3
tries = 0
guess = int(input("Guess a number"))
for tries in range (0,  2):
    if number > guess:
        guess = int(input("Guess higher"))
    elif number < guess:
        guess = int(input("Guess lower"))

print ("the correct number is 3")
