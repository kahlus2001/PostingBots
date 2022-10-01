import tweepy
import json

API_keys_file = r"C:\Users\mikol\Documents\others\twitter_bot_keys.txt"
with open(API_keys_file, "r") as f:
    file_content = f.read()
    keys_dict = json.loads(file_content)

    api_key = keys_dict["api_key"]
    api_secret_key = keys_dict["api_secret_key"]
    access_token = keys_dict["access_token"]
    access_token_secret = keys_dict["access_token_secret"]

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")