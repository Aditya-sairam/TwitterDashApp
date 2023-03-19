from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy

analysis = TextBlob("I don't think that's a good Idea!")
analyser = SentimentIntensityAnalyzer()
vs = analysis.sentiment.polarity
print(float(vs))