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

# Countdown logic
release_date = datetime(2025, 7, 24)
today = datetime.now()
days_left = (release_date - today).days

# List of invisible characters to rotate daily (ensures uniqueness)
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF']
variation = invisible_chars[days_left % len(invisible_chars)]

# Compose tweet only if today is before or on release date
if days_left > 0:
    tweet = f"ఆంధి ఆగమనం మరో {days_left}{variation} రోజుల్లో 💥"
elif days_left == 0:
    tweet = "ఆంధి ఆగమనం\nWatch #HHVM in your nearest theatres"
else:
    tweet = None  # No tweet after release

# Post tweet if applicable
if tweet:
    print("Tweeting:", tweet)
    client.create_tweet(text=tweet)
else:
    print("No tweet today.")
