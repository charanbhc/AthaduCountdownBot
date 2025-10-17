import tweepy
import os
from datetime import datetime, timezone

# Load credentials from environment variables
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Tweepy Client (v2)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Set the release date (UTC for accuracy)
release_date = datetime(2025, 1, 9, tzinfo=timezone.utc)
today = datetime.now(timezone.utc)
days_left = (release_date.date() - today.date()).days

# Rotate invisible characters to avoid duplicate tweet errors
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF']
variation = invisible_chars[days_left % len(invisible_chars)] if days_left >= 0 else ''

# Compose the tweet
if days_left > 0:
    tweet = f"{days_left}{variation} 👑"
elif days_left == 0:
    tweet = "#TheRajaSaab Arrival 😈"
else:
    tweet = None  # No tweet after release day

# Post the tweet if one was created
if tweet:
    print("Tweeting:", repr(tweet))  # shows invisible char in logs
    try:
        client.create_tweet(text=tweet)
        print("Tweet posted successfully.")
    except Exception as e:
        print("Error posting tweet:", e)
else:
    print("No tweet today.")
