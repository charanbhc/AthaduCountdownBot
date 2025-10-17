import tweepy
import os
from datetime import datetime, timezone

# === CONFIG ===
RELEASE_DATE = datetime(2025, 1, 9, tzinfo=timezone.utc)
# ===============

# Load credentials from environment (set in GitHub Secrets)
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate Tweepy client
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Calculate remaining days
today = datetime.now(timezone.utc)
days_left = (RELEASE_DATE.date() - today.date()).days

# Invisible characters (avoid duplicate tweet errors)
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF']
variation = invisible_chars[days_left % len(invisible_chars)] if days_left >= 0 else ''

# Compose tweet text
if days_left > 0:
    tweet = f"{days_left}{variation} 👑"
elif days_left == 0:
    tweet = "#TheRajaSaab Arrival 😈"
else:
    tweet = None  # stop tweeting after release date

# Post tweet
if tweet:
    print("Tweeting:", repr(tweet))
    try:
        client.create_tweet(text=tweet)
        print("✅ Tweet posted successfully.")
    except Exception as e:
        print("❌ Error posting tweet:", e)
else:
    print("No tweet today.")
