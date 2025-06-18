import tweepy
import os
from datetime import datetime

# Load credentials from GitHub Secrets
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate using Tweepy Client (API v2)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Countdown logic
release_date = datetime(2025, 8, 9)
today = datetime.now()
days_left = (release_date - today).days

# Compose tweet
if days_left > 0:
    # Insert invisible character to avoid duplicate error
    tweet = f"Get Ready #DHFM's {days_left}\u200B days to go 🔁💥"
elif days_left == 0:
    tweet = "#Athadu4k Re-Release is Here! 💥\nIn Theatres Today — Celebrate #DHFM like never before 🔁🎬"
else:
    tweet = (
        "🎉 Happy Birthday to our DemiGod @urstrulymahesh!\n"
        "#Athadu4k Re-Release was on August 9 ❤️"
    )

# Post the tweet
print("Tweeting:", tweet)
client.create_tweet(text=tweet)
