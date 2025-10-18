import tweepy
import os
from datetime import datetime, timezone

# === CONFIG ===
RELEASE_DATE = datetime(2025, 1, 9, tzinfo=timezone.utc)
# ===============

# Load credentials from environment (GitHub Actions secrets!)
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

def ensure(val, name):
    if not val:
        raise ValueError(f"Missing environment variable: {name}")

# Assert all required secrets are present
ensure(bearer_token, "BEARER_TOKEN")
ensure(consumer_key, "API_KEY")
ensure(consumer_secret, "API_SECRET")
ensure(access_token, "ACCESS_TOKEN")
ensure(access_token_secret, "ACCESS_TOKEN_SECRET")

# Authenticate Tweepy client (OAuth 1.0a + OAuth2 bearer)
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

# Add invisible character for duplicate tweet prevention
invisible_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF']
variation = invisible_chars[days_left % len(invisible_chars)] if days_left >= 0 else ''

# Compose tweet
if days_left > 0:
    tweet = f"{days_left}{variation} 👑"
elif days_left == 0:
    tweet = "#TheRajaSaab Arrival 😈"
else:
    tweet = None

# Post tweet if needed
if tweet:
    print("Tweeting:", repr(tweet))
    try:
        response = client.create_tweet(text=tweet)
        # Print tweet ID for debugging
        print("✅ Tweet posted. Tweet ID:", response.data.get('id') if hasattr(response, 'data') else response)
    except Exception as e:
        print("❌ Error posting tweet:", repr(e))
else:
    print("No tweet today.")
