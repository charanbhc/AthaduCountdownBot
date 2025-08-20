import tweepy
import os
from datetime import datetime

# Load credentials from environment variables
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Tweepy
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Set the release date
release_date = datetime(2025, 9, 25)
today = datetime.now()
days_left = (release_date - today).days

# Rotate invisible characters to avoid duplicate tweet errors
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF']
variation = invisible_chars[days_left % len(invisible_chars)] if days_left >= 0 else ''

# Compose tweet
if days_left > 0:
    tweet = f"#OG ఆగమనం మరో {days_left}{variation} రోజుల్లో 🐆"
elif days_left == 0:
    tweet = "#TheyCallHimOG Day\nWatch #TheyCallHimOG in your nearest theatres"
else:
    tweet = None  # No tweet after release day

# Post the tweet if one was created
if tweet:
    print("Tweeting:", repr(tweet))  # Shows invisible char in logs
    client.create_tweet(text=tweet)
else:
    print("No tweet today.")
