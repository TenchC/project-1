"""
  Tench Cholnoky
  Radical Software, Fall 2021
  Project 1
  Sept 23, 2021
  python3
"""

import tweepy
import random

#import twitter bot authorizations
from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

message = ""

api = tweepy.API(auth)
mentions = api.mentions_timeline()
mention_tweet = random.choice(mentions)

#splits the words into a list
mention_tweet_words = mention_tweet.text.split()


#define the function of list 2 string
def list_to_string(mention_tweet_words):
    str1 = ""
    return (str1.join(mention_tweet_words))

#function of list turned into string
tweet_string = list_to_string(mention_tweet_words)

#find the question mark and make a question test variable
question_test = tweet_string.find("?")

#if a question mark is in the string it will return its position, which will always
#be higher than 1. If there is no question mark, the find command will return a -1
if question_test > -1:
    answer_list = ["~yes~", "~no~", "~maybe~", "~at some point soon~", "~try again~",
    "~outlook good~","~doubtful~", "~it is certain~", "~my sources say no~"]
    answer = random.choice(answer_list)

    #basic formatting
    print("I responded to:")
    print("' " + mention_tweet.text + " '")
    print("")
    message = (" Thank you for your question, my answer is... " + answer)
    #add the @ to the mention
    message = "@" + mention_tweet.user.screen_name + message
    print("I tweeted:")
    print(message)
    api.update_status(message, in_reply_to_status_id=mention_tweet.id)

else:
#no question mark
    #basic formatting
    print("I responded to:")
    print("' " + mention_tweet.text + " '")
    print("")

    message = (" Please ask me a question")
    #add the @ to the mention
    message = "@" + mention_tweet.user.screen_name + message
    api.update_status(message, in_reply_to_status_id=mention_tweet.id)
    print("I tweeted:")
    print(message)
