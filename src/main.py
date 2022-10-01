from src.twitter_bot import make_api

def run():
    api = make_api()
    api.update_status("Test tweet from Tweepy Python")


if __name__ == '__main__':
    run()