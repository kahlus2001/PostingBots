import tweepy
import json
import os

API_keys_file = os.getenv("api_keys_file")
with open(API_keys_file, "r") as f:
    file_content = f.read()
    keys_dict = json.loads(file_content)

    api_key = keys_dict["api_key"]
    api_secret_key = keys_dict["api_secret_key"]
    access_token = keys_dict["access_token"]
    access_token_secret = keys_dict["access_token_secret"]
    clientID = keys_dict["clientID"]
    client_secret = keys_dict["client_secret"]


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")

api.update_status("Test tweet from Tweepy Python")