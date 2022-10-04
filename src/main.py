import time

from src.make_content import connect_quotes_api, connect_images_api, make_post_content
from src.twitter_bot import make_bot_connection, tweet


def run():
    """ Main run point of app. """

    posting_frequency = 10800   # 3 hours in seconds
    api = make_bot_connection()
    connect_quotes_api()
    connect_images_api()

    while True:
        content = make_post_content()
        tweet(api, content)
        time.sleep(posting_frequency)


if __name__ == '__main__':
    run()
