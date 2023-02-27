from src.TwitterAutomationSolutions.twitter_bot import make_bot_connection, tweet


def run():
    """ Main run point of app. """

    posting_frequency = 10800   # 3 hours in seconds
    api = make_bot_connection()
    tweet(api)

    # while True:

    #     tweet(api)
    #     time.sleep(posting_frequency)


if __name__ == '__main__':
    run()
