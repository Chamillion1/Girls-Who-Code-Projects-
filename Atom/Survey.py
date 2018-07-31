import json
import os

questions = ["What is your name?", "Who is your favorite cartoon character?", "Which amusement or theme park is your favorite?", "Who is your favorite singer or band?", "What is your favorite video game?", "What is your favorite holiday?", "What are your hobbies or interests?", "What is your favorite movie?", "What is your favorite TV show?", "Who is your favorite Disney princess?", "What is your favorite quote from any movie?", "Who is your favorite Marvel superhero or villain?", "What do you prefer Marvel or DC?", "Who is your favorite Harry Potter character?", "Which Hogwarts House are you sorted in?"]
answers = []
cont = True
data = []
while cont:
    answer = {}
    for q in questions:
        answer[q] = input(q)
    to_cont = input("Continue? Y/N ")
    if to_cont == "Y":
        cont = True
    else:
        cont = False
    answers.append(answer)

    print(answer)

f = open("list_of_answers.json", "r+")     # Create a file called data.json, with the write permission
json_obj = json.dumps(list_of_answers)    # Turn data (list of dictionaries) into a json object
f.write(json_obj) # Write the json object to our file
f.close() #
