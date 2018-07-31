# Starter code for a riddle game
# The user has N tries to guess the answer to a riddle
# After the first attempt, give the user a hint for each attempt

def display(riddle, try_number, hint_list):
    '''
    Given the riddle and number of attempts, the function
    displays number of attempts and the riddle question
    input: riddle (string), try_number(integer), hint_list (list of strings)
    output (return value): N/A
    '''
    # TODO: Print the attempt number and the riddle question
    def greeting():
        "Do you think you can solve this riddle? Let's find out"

    # Print a hint if not the first attempt
    if try_number > 0:
        print("HINT: {}".format()) # TODO: Access hint_list for a hints


def riddle():
    # Initialize our variables
    guess_count = 3                   # Keeps track of the number of guesses (need if using a while loop)
    riddle = "It is shorter than the rest, but when you are happy, you raise it up like it is the best. What is it?"     # TODO: The riddle
    answer = "thumb"                 # TODO: The answer to the riddle; can be a string or list of possible answers
    hints = ["It's Tweedle Dee's twin brother","It's on your hand"]      # TODO: List of hints; number of hints == number of allowed attempts - 1
                                      # i.e. if 3 guesses allowed, need 2 hints
    guess = None                      # Keep track of the user's guess
    win = False                       # Keep track of whether the user has won

    # Use a loop that gives the user 3 tries to guess the answer to the riddle

        # TODO: Call "display" function (with the right parameters!!)
        # and print out the riddle prompt, attempt number,
        # and hints if not the first try

        # TODO: Get user input and process it
        guess = input("Enter your guess here:  ").lower().rstrip()

        # TODO: Check if answer is correct

            # TODO: Set variable "win" to True and break out of loop

    # TODO: Print different messages for winning and losing.
print("Incorrect! The correct answer is {}".format(answer))

print("Game Over! Thanks for playing! :)")
