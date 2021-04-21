# Scraping Data From Twitter
# Evelina Ramoskaite
# API Key
# T79OGk7rOw7EoKLvlemIrtACE
#API Secret Key
# Kb9clPlQjsICv6VU6AJPezSEA98qj13yFgzKUq2BSmAyZdk6if
#Bearer Token
# AAAAAAAAAAAAAAAAAAAAAK0HOwEAAAAAWOu9MKUs1gZLYsSNxDmxBWCwU84%3DA7KbUUblBvzm139nB2z6hdB4v1ioRO7ZzxVhgVdl6tLizJc4OT
# Access Token
# 1382438548243161089-c7zmGHAu9XRwR1XUUPZ0aM9mLyXVpU
# Access Token Secret
# A7zNllSD367Vd5EAo95wbmaiNBeT9ucrB3qg849Sl3fVC
import tweepy
import csv
import re
import json

print("hello")


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    # create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # initialize Tweepy API
    api = tweepy.API(auth)



    # open the spreadsheet we will write to
    with open('hastag%s.csv'%(spreadsheetName),'w',encoding='utf-8') as file:
        w = csv.writer(file)

        # write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        # for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase + ' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n', ' ').encode('utf-8'),
                        tweet.user.screen_name.encode('utf-8'),
                        [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])

spreadsheetName= input('filename ')
consumer_key = 'T79OGk7rOw7EoKLvlemIrtACE'
consumer_secret = 'Kb9clPlQjsICv6VU6AJPezSEA98qj13yFgzKUq2BSmAyZdk6if'
access_token = '1382438548243161089-c7zmGHAu9XRwR1XUUPZ0aM9mLyXVpU'
access_token_secret = 'A7zNllSD367Vd5EAo95wbmaiNBeT9ucrB3qg849Sl3fVC'

hashtag_phrase = input('Hashtag Phrase ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)