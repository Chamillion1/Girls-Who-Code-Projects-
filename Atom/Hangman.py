# Have a word/ phrase
phrase "girls who code"

# Keep track of user's guesses
guessed_letters = []
# Keep track of bad letters
bad = []
# Keep track of good letters
good = []

# Tell the user how many spaces and letters
display = ""
for letter in phrase:
    if letter in guessed_letters:
        display += letter
        # Processing the space in our phrase
    elif letter == " ":
        display += "  "
        # the letter in our phrases has not been guessed yet
    else:
        display += "_ "
print (display)

    # Allow user to give input to computer
guess = input("Enter a letter: ")
# Tell the user if they get the right letter
        # Add the good letter to our good letter
        if guess in phrase:
            print("You got a letter: {}" .format(guess))
guessed_letters.append(guess)

# Tell user how many spaces and letters they need to guess
display = ""
for letter in phrase:
    if letter in guessed_letters:
        display += letter
        # Processing the space in our phrase
    elif letter == " ":
        display += " "
        # The letter in our phrases has not been guessed yet








# Tell the user if they get the wrong letter

# End the game if the user gets all the right letters in our word/ phrase
