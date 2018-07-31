# --- Define your functions below!---
def Intro():
    print("Hello! Welcome to the chatbot!")
def greeting():
    print("Let's have a deep conversation")
    def dating():
        print("I am 105 years old. I am a Fashion Nova Instagram Model in my free time.")
        print("During the day, I am a cereal eater. At night I am Batman.")
        rep = input("Soooo, come here often? ")

dating_prompt = ['Hello ;)','love me','Come here often?','I need a partner in crime']
art_prompt = ['draw me,''art', 'draw please' ]
# --- Put your main program below! ---
def main():
    valid_input = ["Hi!", 'Hello ;) ', 'love me','Come here often?', 'I need a partner in crime', 'draw me', 'art', 'draw please']
    Intro()

    while True:
     answer = input("(What will you say?)")
     if answer == "Hi!":
        greeting()
        if response in all_valid_inputs:
            return True
        else:
            return False
     elif answer in dating_prompt:
        dating()
     elif answer in ['draw me', 'art', 'draw please']:
        artist()

    else:
        print("These are the inputs I understand: ")
        for vi in valid_input:
            print
        print("Say 'Hi!'; I don't understand anything else")

 # DON'T TOUCH! Setup code that runs your main () function
if  __name__ == "__main__":
    main()
