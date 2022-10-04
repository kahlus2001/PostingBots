import tweepy
import json
import os
import logging

logger = logging.getLogger()


def make_bot_connection():
    """ Initialize API connection with Twitter.

    Raises
    ------
    Exception as e
        If could not initialize Twitter API connection.

    Returns
    --------
    tweepy.api.API
        Connected API object
    """

    api_keys_file = os.getenv("api_keys_file")
    with open(api_keys_file, "r") as f:
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
        logging.info("Authentication OK.")
    except Exception as e:
        logging.error("Error during authentication.")
        raise e
    return api


def tweet(api, content):
    """ Tweet content on Twitter.

    Parameters
    ----------
    api : tweepy.api.API
        The tweepy Twitter API object
    content : PIL.PngImagePlugin.PngImageFile
        Image with quote of .png format

    Raises
    ------
    Exception as e
        If could not tweet.
    """

    try:
        api.update_status(content)
        logging.info("Tweeted successfully!")
    except Exception as e:
        logging.error("Could not tweet.")
        raise e

