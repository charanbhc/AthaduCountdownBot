import tweepy
import os
from datetime import datetime, timezone

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

# Set the release date with UTC timezone and time at start of day
release_date = datetime(2026, 1, 9, tzinfo=timezone.utc)

# Get current date in UTC timezone (to avoid timezone issues)
today = datetime.now(timezone.utc)

# Calculate days left ignoring hours/minutes by using date only
days_left = (release_date.date() - today.date()).days

# Rotate invisible characters to avoid duplicate tweet errors
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF']
variation = invisible_chars[days_left % len(invisible_chars)] if days_left >= 0 else ''

# Compose tweet
if days_left > 0:
    tweet = f" {days_left}{variation} 👑"
elif days_left == 0:
    tweet = "#TheRajaSaab Arrival 😈"
else:
    tweet = None  # No tweet after release day

# Post the tweet if one was created
if tweet:
    print("Tweeting:", repr(tweet))  # Shows invisible char in logs
    client.create_tweet(text=tweet)
else:
    print("No tweet today.")
