#Tench Cholnoky's Python Haiku Bot
#So powerful, so profound
import tweepy
import random

from authorization_tokens import *

message = ""
first_line = []
second_line = []
third_line = []
syllable_counter = 0
syllable_list1 = ["one ", "day ", "change ", "to ", "can ", "I ", "we ", "of ",
"old ", "new ", "pond ", "breeze ", "the " "fire "]
syllable_list2 = ["toucan ", "water ", "river ", "baby ", "engulf ", "mountain ",
"monster ", "sunrise ", "sunset ", "reflection", "silence ", "autumn ", "sunshine ",
"winter "]
syllable_list3 = ["creative ", "traveller ", "waterfall ", "abandon ", "favorite ",
"prisoner ", "unity ", "moonlight ", "origin "]

# basic structure for lines, 5+7+5

#counter to decide the first word, start with counter 123 and any_word

syllable_counter123 = [1, 2, 3]
any_word = random.choice(syllable_counter123)

#if there are 3 syllables it can only choose between 1 and 2 syllable words
syllable_counter12 = [1, 2]
med_word = random.choice(syllable_counter12)

#if there are 4 syllables then it can only choose 1 syllable words





#5 SYLLABLE LINE
print("loading Haiku...")
#picking the first word
if any_word == 3:
    first_line.append(random.choice(syllable_list3))
    syllable_counter = syllable_counter + 3
elif any_word == 2:
    first_line.append(random.choice(syllable_list2))
    syllable_counter = syllable_counter + 2
else:
    first_line.append(random.choice(syllable_list1))
    syllable_counter = syllable_counter + 1

print("adding words...")
#check how many syllables are put in line one so far
while syllable_counter < 5:
    #if there are 2 or less syllables, repeat this process
    if syllable_counter <= 2:
        any_word = random.choice(syllable_counter123)
        if any_word == 3:
            first_line.append(random.choice(syllable_list3))
            syllable_counter = syllable_counter + 3
        elif any_word == 2:
            first_line.append(random.choice(syllable_list2))
            syllable_counter = syllable_counter + 2
        else:
            first_line.append(random.choice(syllable_list1))
            syllable_counter = syllable_counter + 1

    #if there are 3 syllables, a 3 syllable word is not an option
    elif syllable_counter == 3:
        med_word = random.choice(syllable_counter12)
        if med_word == 2:
            first_line.append(random.choice(syllable_list2))
            syllable_counter = syllable_counter + 2
        elif med_word == 1:
            first_line.append(random.choice(syllable_list1))
            syllable_counter = syllable_counter + 1

    #if there are 4 syllables, it can only pick from 1 syllable words
    elif syllable_counter == 4:
        first_line.append(random.choice(syllable_list1))
        syllable_counter = syllable_counter + 1


#changing list of words to a string
#defining the function
def list_to_string(first_line):
    str1 = ""

    return (str1.join(first_line))









#this is to decide the first word, it picks randomly from 1, 2, and 3 syllables
print("loading second line...")
syllable_counter = 0
if any_word == 3:
    second_line.append(random.choice(syllable_list3))
    syllable_counter = syllable_counter + 3
elif any_word == 2:
    second_line.append(random.choice(syllable_list2))
    syllable_counter = syllable_counter + 2
else:
    second_line.append(random.choice(syllable_list1))
    syllable_counter = syllable_counter + 1

    #check how many syllables are put in line one so far
print("mixing it up...")
while syllable_counter < 7:
    #if there are 2 or less syllables, repeat this process
    if syllable_counter <= 4:
        any_word = random.choice(syllable_counter123)
        if any_word == 3:
            second_line.append(random.choice(syllable_list3))
            syllable_counter = syllable_counter + 3
        elif any_word == 2:
            second_line.append(random.choice(syllable_list2))
            syllable_counter = syllable_counter + 2
        else:
            second_line.append(random.choice(syllable_list1))
            syllable_counter = syllable_counter + 1
    #if there are 5 syllables, a 3 syllable word is not an option
    elif syllable_counter == 5:
        med_word = random.choice(syllable_counter12)
        if med_word == 2:
            second_line.append(random.choice(syllable_list2))
            syllable_counter = syllable_counter + 2
        elif med_word == 1:
            second_line.append(random.choice(syllable_list1))
            syllable_counter = syllable_counter + 1
    #if there are 6 syllables, it can only pick from 1 syllable words
    elif syllable_counter == 6:
        print("engaging in serious introspection...")
        second_line.append(random.choice(syllable_list1))
        syllable_counter = syllable_counter + 1

#changing list of words to a string

#defining the function
def list_to_string(second_line):
    str2 = ""

    return (str2.join(second_line))








#5 SYLLABLE LINE
syllable_counter = 0
print("wrapping up...")
if any_word == 3:
    third_line.append(random.choice(syllable_list3))
    syllable_counter = syllable_counter + 3
elif any_word == 2:
    third_line.append(random.choice(syllable_list2))
    syllable_counter = syllable_counter + 2
else:
    third_line.append(random.choice(syllable_list1))
    syllable_counter = syllable_counter + 1

#check how many syllables are put in line so far
print("scrapping this god awful poem...")
while syllable_counter < 5:
    #if there are 2 or less syllables, repeat this process
    if syllable_counter <= 2:
        any_word = random.choice(syllable_counter123)
        if any_word == 3:
            third_line.append(random.choice(syllable_list3))
            syllable_counter = syllable_counter + 3
        elif any_word == 2:
            third_line.append(random.choice(syllable_list2))
            syllable_counter = syllable_counter + 2
        else:
            third_line.append(random.choice(syllable_list1))
            syllable_counter = syllable_counter + 1
    #if there are 3 syllables, a 3 syllable word is not an option
    elif syllable_counter == 3:
        med_word = random.choice(syllable_counter12)
        if med_word == 2:
            third_line.append(random.choice(syllable_list2))
            syllable_counter = syllable_counter + 2
        elif med_word == 1:
            third_line.append(random.choice(syllable_list1))
            syllable_counter = syllable_counter + 1
    #if there are 4 syllables, it can only pick from 1 syllable words
    elif syllable_counter == 4:
        print("feeling it out...")
        third_line.append(random.choice(syllable_list1))
        syllable_counter = syllable_counter + 1


#changing list of words to a string

#defining the function
def list_to_string(third_line):
    str3 = ""

    return (str3.join(third_line))

#final punctuation
punctuation = ["!", "?", "...", ".", "~"]
final_punctuation = random.choice(punctuation)

#authorize twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#tweet yo!
api = tweepy.API(auth)
api.update_status("Here is a haiku for you: " + list_to_string(first_line) + ", " + list_to_string(second_line) + ", " + list_to_string(third_line) + final_punctuation)
print("I tweeted '" + list_to_string(first_line) + ", " + list_to_string(second_line) + ", " + list_to_string(third_line) + final_punctuation + "'")
