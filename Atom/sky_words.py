'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the twitter data you
need!
'''

import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pylot as plt

# Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity_values = []

for tweet in tweetData:
    tweets.append(tweet["text"])
giant_string = " ".join(tweets)

# Dictionary of the frequency of each word
# key = words, value = count/ frequency of the words appearance
list_of_words = giant_string.split()

word_count = {}
for word in list_of_words:




for word in list_of_words:
    word = word.lower().rstrip().lstrip()
    if "http" in word:
        continue
    if word[0] in {",", "?", ".", ":", "/", "!", '"', "'"}:
        word = word[:-1]
    if len(word) < 4:
        continue
    if word[-1] in {",", "?", ".", ":", "/", '"', "'"}:
        word = word[:-1]

        word_polarity = TextBlob(word).polarity
    if word_polarity , -0.25
