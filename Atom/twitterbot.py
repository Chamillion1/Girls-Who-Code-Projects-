# Imports
import tweepy
import random
import time
#Keys and Access Tokens
CONSUMER_KEY  =
CONSUMER_SECRET =

ACCESS_TOKEN   =
ACCESS_SECRET  =


tweets = ["you are a snacc", "are you google? cuz i just found what i was looking for", "I'm no photographer, but I can picture us together", "Are you Australian? Because you meet all of my koala-fications"]

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count += 1
    index.random.randint (0, len(tweets) -1)
    api.update_status(tweets[index]+ str(count)) # randomly a tweet from tweets
