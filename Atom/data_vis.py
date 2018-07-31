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


    tb = TextBlob(tweet_text)
    print("{}: {}".format(tweet_text, tb.polarity))
    polarity_values.append(tb.polarity)

# bins = [-1, -0.5, 0, 0.5, 1]

plt.hist(polarity_values, bins)
plt.title("tweet polarity")
plt.ylabel("Count of tweets")
plt.xlabel("Polarity")
plt.show()
