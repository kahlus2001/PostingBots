import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters
import requests
import json
import logging
import io


def get_quote():
    """ GET random quote from Quotes API.

    Returns
    -------
    text: str
        text fetched from Quotes API
    """

    try:
        # making the get request
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            # extracting the core data
            json_data = response.json()
            data = json_data['data'][0]

            # getting the quote from the data
            quote = data['quoteText']
            author = data['quoteAuthor']
            text = quote + '\n' + author
            return text
        else:
            print("Error while getting quote")
    except Exception as e:
        print("Something went wrong! Try Again!")
        raise e


def get_background_img():
    """ Get random background image from Images API.

    Returns
    -------
    image: PIL.PngImagePlugin.PngImageFile
        image fetched from images API
    """

    api_keys_file = os.getenv("image_api_keys")
    with open(api_keys_file, "r") as f:
        file_content = f.read()
        keys_dict = json.loads(file_content)
        access_key = keys_dict["access_key"]
        secret_key = keys_dict["secret_key"]

    # get images info from API

    url = f"https://api.unsplash.com/photos/?client_id={access_key}&query=nature"
    try:
        # Making the get request
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(response)

            # Extracting image from API data
            json_data = response.json()
            image_download = json_data[0]["links"]["download"]
            download = requests.get(image_download)
            image_bytes = download.content
            image = Image.open(io.BytesIO(image_bytes))
            return image
        else:
            print("Error while getting image")
    except Exception as e:
        print("Something went wrong! Try Again!")
        raise e


def write_quote_on_image(quote, image):
    """ Write quote with chosen font on image.

    Parameters
    ----------
    quote : st
    image : PIL.PngImagePlugin.PngImageFile
        image object

    Returns
    ------
    img: PIL.PngImagePlugin.PngImageFile
        Image with quote on it with .png format
    """
    # Choosing font size
    image_width, image_height = image.size
    quote_len = len(quote)
    font_size = int(image_width / 20)

    font = ImageFont.truetype(font=r"C:\Windows\Fonts\Arial.ttf", size=font_size)
    avg_char_width = sum(font.getlength(char) for char in ascii_letters) / len(ascii_letters)
    max_char_count = int((image_width * .95) / avg_char_width)
    text = textwrap.fill(text=quote, width=max_char_count)

    I1 = ImageDraw.Draw(image)
    I1.multiline_text(xy=(image.size[0]/2, image.size[1] / 2), text=text, font=font, fill='#000000', anchor='mm')
    image.show()
    # img.save("image.png")
    return image


def make_post_content():
    """ Create a new instance of image with quote to be tweeted.

    Returns
    ------
    content: PIL.PngImagePlugin.PngImageFile
        Image with quote of .png format
    """

    quote = get_quote()
    image = get_background_img()
    content = write_quote_on_image(quote, image)
    return content
