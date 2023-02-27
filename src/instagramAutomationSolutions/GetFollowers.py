import re
import requests
from bs4 import BeautifulSoup


def get_followers_count(username):
    # Send a GET request to the Instagram account's page
    url = f'https://www.instagram.com/{username}/'
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the number of followers
    follower_count_text = soup.find('meta', property='og:description')['content']

    # Extract the number of followers from the element using regular expressions
    follower_count = re.search(r'([0-9,.]+) Followers', follower_count_text).group(1)

    # Return the number of followers
    return follower_count


print(get_followers_count('mikolaj_kahl'))
