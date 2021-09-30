"""
  Tench Cholnoky
  Radical Software, Fall 2021
  Project 1 Final
  Sept 25, 2021
  python3
"""

#twitter authorizations
import tweepy
import random
from authorization_tokens import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#most recent mention
mentions = api.search(q="data", lang="en")
tweet = random.choice(mentions)

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

if location == []:
    location = "none"


    #first half of the data
message_1 = " tweeter data part 1: Location: {}, follower count: {}, friend count: {}, user created at: {} UTC, time zone: {}, geotagging enabled: {}, verified: {}."
message_1 = message_1.format(location, followers_count, friends_count, created_at, time_zone, geo_enabled, verified)
message_1 = tweet.user.screen_name + message_1

    #second half of the data
message_2 = " tweeter data part 2: Status count: {}, profile color: {}, default profile image: {}, am I following you: {}, have I requested to?: {}, withheld in countries: {}."
message_2 = message_2.format(status_count, profile_color, default_profile_image, following, follow_request_sent, withheld_in_countries)
message_2 = "@bot_tench " + tweet.user.screen_name + message_2

#Print tweets and format
print("Tweet One:")
print("")
print(message_1)
print("")
print("Tweet Two:")
print("")
print(message_2)
    #tweeting out the data


api.update_status(message_1)

    #respond to first tweet
timeline = api.user_timeline(count = 1)
timeline = random.choice(timeline)
user_id = timeline.id
api.update_status(message_2, in_reply_to_status_id=user_id)
