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





def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase, date_since="2021-04-28", date_end="2021-04-29"):
    # create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # initialize Tweepy API
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)



    # open the spreadsheet we will write to
    with open('hastag%s.csv'%(spreadsheetName),'w',encoding='utf-8') as file:
        w = csv.writer(file)

        # write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text','all_hashtags','retweet_count', 'tweet_created_at',' username', 'followers_count'])


        # for each tweet matching our hashtags, write relevant info to the spreadsheet
        backoff_counter = 1
        while True:
            try:
                for tweet in tweepy.Cursor(api.search,q=hashtag_phrase + ' -filter:retweets', \
                                           lang="en",since= date_since,until=date_end, tweet_mode='extended').items(100000): # iterating over first 100,000 tweets
                    w.writerow([tweet.created_at,
                                tweet.full_text.replace('\n', ' ').encode('utf-8'),                       # tweet text
                                [e['text'] for e in tweet._json['entities']['hashtags']],                 # hashtags
                                tweet.retweet_count,                                                      # retweet count
                                tweet.created_at,                                                         # tweet created at
                                tweet.user.screen_name.encode('utf-8'),                                   # username
                                tweet.user.followers_count],                                              # user followers
                                )
                break
            except tweepy.TweepError as e:
                print(e.reason)
                sleep(60*backoff_counter)
                backoff_counter += 1
                continue


spreadsheetName= input('filename hashtag ______:  ')               # enter desired name for output file
consumer_key = 'T79OGk7rOw7EoKLvlemIrtACE'
consumer_secret = 'Kb9clPlQjsICv6VU6AJPezSEA98qj13yFgzKUq2BSmAyZdk6if'
access_token = '1382438548243161089-c7zmGHAu9XRwR1XUUPZ0aM9mLyXVpU'
access_token_secret = 'A7zNllSD367Vd5EAo95wbmaiNBeT9ucrB3qg849Sl3fVC'

hashtag_phrase = input('Stock Hashtag: ')           # enter stock hashtag



if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)