# Import libraries
import json

file = open("tweets.json", "r")
data = json.load(file) #load from file into a json project

for d in data: # data is a list, d is a dictonary
#  Loop through the dictionary (which corresponds to a single
#  tweet)

    # TO PRINT OUR DICTIONARY
#  for info_category, info in d.items():
#    #print(info_category, info)

# TO PRINT THE ACTUAL TEXT OF OUR TWEET
    # d is our dictionary about our tweet
    # for user_mention in d["user_mentions"]:
          # Each user_mention is a dictionary
        # it corresponds
        print(d["user_mentions"]:
    break
