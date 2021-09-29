"""
  Tench Cholnoky
  Radical Software, Fall 2021
  Project 1 Final
  Sept 25, 2021
  python3
"""

#twitter authorizations
import tweepy
from authorization_tokens import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#most recent mention
mentions = api.mentions_timeline()
tweet = mentions[0]

#grab all the goodies
location = tweet.user.location
followers_count = tweet.user.followers_count
friends_count = tweet.user.friends_count
created_at = tweet.user.created_at
time_zone = tweet.user.time_zone
geo_enabled = tweet.user.geo_enabled
verified = tweet.user.verified
status_count = tweet.user.statuses_count
profile_color = tweet.user.profile_background_color
default_profile_image = tweet.user.default_profile_image
following = tweet.user.following
follow_request_sent = tweet.user.follow_request_sent
notifications = tweet.user.notifications
translator_type = tweet.user.translator_type
withheld_in_countries = tweet.user.withheld_in_countries

if withheld_in_countries == []:
    withheld_in_countries = "none"

#check for consent
tweet_consent = tweet.text.split()

#define the function of list 2 string
def list_to_string(tweet_consent):
    str1 = ""
    return (str1.join(tweet_consent))

tweet_string = list_to_string(tweet_consent)

#if the consent check is good go through with the tweet, otherwise tweet
#different message plz
if tweet_string == "@bot_tenchiconsenttomydatabeingpubliclydisplayed":
    print("Participant consented")

    #first half of the data
    message_1 = " part 1: Location: {}, follower count: {}, friend count: {}, user created at: {} UTC, time zone: {}, geotagging enabled: {}, verified: {}."
    message_1 = message_1.format(location, followers_count, friends_count, created_at, time_zone, geo_enabled, verified)
    message_1 = "@" + tweet.user.screen_name + message_1

    #second half of the data
    message_2 = " part 2: Status count: {}, profile color: {}, default profile image: {}, am I following you: {}, have I requested to?: {}, withheld in countries: {}."
    message_2 = message_2.format(status_count, profile_color, default_profile_image, following, follow_request_sent, withheld_in_countries)
    message_2 = "@" + tweet.user.screen_name + message_2

    print(message_1)
    print(message_2)
    #tweeting out the data
    api.update_status(message_1, in_reply_to_status_id=tweet.id)
    api.update_status(message_2, in_reply_to_status_id=tweet.id)


#if they didn't type exactly the right thing
else:
    reject_message = "@" + tweet.user.screen_name + " to get your data publicly displayed please tweet me 'i consent to my data being publicly displayed' no caps :-)"
    api.update_status(reject_message, in_reply_to_status_id=tweet.id)
