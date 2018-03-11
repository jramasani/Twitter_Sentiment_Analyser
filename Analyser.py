import tweepy
from textblob import TextBlob
import sys
import csv

consumer_key = 'l9IIjXEFUOF17cqRhYjgryQv7'
consumer_secret = 'Rh15VRkJz7gPGhBrLwZNrc2m7LydaF6IqIXT4xt3AW7GBswTNM'

access_token_key = '765951620953825280-tVmx5437WidqCRp9TJNIVIcMjkp4tlN'
access_token_secret = 'SqN48dNqHW7mIKMbn5FH1cRq44DWUbIgQ6mbvTloEEeyK'

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