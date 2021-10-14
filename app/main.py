# Eli McGehee's Twitter Bot for TNS RS 2021

# Imports/Constants
import tweepy
import random
import time
from authorization_tokens import *
from messages import *

# Authentication Codes
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Bot Start Functions
beepboop2 = random.choice(beepboop)
named_tuple = time.localtime() 
time_string = time.strftime("%m/%d/%Y", named_tuple)
location = "(" + time_string + ")"

api.update_profile(location = beepboop2 + SPACE + location + SPACE + online)

# Main Function
billionaires = [ JeffBezos, ElonMusk, MarkZuckerberg, WarrenBuffet, LarryEllison ]
randomarticles = random.choice(articles)
randombillionaires = random.choice(billionaires)
randomemojis = random.choice(startemojis)

api.update_status(randomemojis + SPACE + randombillionaires + SPACE + randomarticles)

# Delay/Stop
time.sleep(60)
api.update_profile(location = beepboop2 + SPACE + location + SPACE + offline)

# Custom Phrase List for the Terminal
done = random.choice(phrase_list)
print(done)

