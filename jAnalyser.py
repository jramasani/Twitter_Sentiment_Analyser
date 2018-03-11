import tweepy
from textblob import TextBlob
import sys
import csv

consumer_key = #YOUR CONSUMER KEY HERE
consumer_secret = #YOUR CONSUMET SECRET HERE

access_token_key = #YOUR ACCESS TOKEN HERE
access_token_secret = #YOUR ACCESS TOKEN SECRET HERE

auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
auth.set_access_token(access_token_key, access_token_secret);

api = tweepy.API(auth)


if len(sys.argv) >= 2:
	topic = sys.argv[1]
else:
	print("By default topic is Modi.")
	topic = "Modi"


public_tweets = api.search(q=topic, count=500)
tweets_list = []
with open('sentiment.csv', 'w', newline='\n') as  f:
    writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment', 'Polarity', 'Subjectivity'])
    writer.writeheader()
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text);
        polarity = analysis.sentiment.polarity;
        subjectivity = analysis.sentiment.subjectivity;
        if polarity >= 0:
            sentiment = 'positive';
        else:
            sentiment = 'negative';
        writer.writerow({'Tweet': tweet.text, 'Sentiment': sentiment, 'Polarity': polarity, 'Subjectivity':subjectivity})