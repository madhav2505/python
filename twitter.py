
# coding: utf-8

# In[ ]:


import tweepy
import json
import time

# Twitter API Keys
consumer_key = "Z67A0R8jHz9rhRyiKMkBTWQaw"
consumer_secret = "LsUUeETmw7SPWYWNk5xVMyNuoFdwtzxSKsAZ5WdHsQ0XwOCVXz"
access_token = "903741141413232640-ct74VPTMlgOsSRR488gz8QHYdZHA6bA"
access_token_secret = "zQiHkBxwpd0XTbAHIc1gStoes20YoeoHm9T5Dr76Fjufs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):

    api.update_status("This is tweet #%s, but with a timer man!" % tweet_number)


# Create a loop that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

