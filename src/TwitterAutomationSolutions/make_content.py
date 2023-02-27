import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters
import requests
import uuid


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
    """ Get random background from a directory with images.

    Returns
    -------
    image: PIL.PngImagePlugin.PngImageFile
        image fetched from directory
    """

    source_dir = os.getenv('backgrounds')
    imgs = os.listdir(source_dir)
    img = random.choice(imgs)
    full_img_path = os.path.join(source_dir, img)
    image = Image.open(full_img_path)
    return image


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
    middle_position = (image.size[0]/2, image.size[1] / 2)

    font = ImageFont.truetype(font=r"C:\Windows\Fonts\Arial.ttf", size=font_size)
    avg_char_width = sum(font.getlength(char) for char in ascii_letters) / len(ascii_letters)
    max_char_count = int((image_width * .95) / avg_char_width)
    text = textwrap.fill(text=quote, width=max_char_count)

    img = ImageDraw.Draw(image)
    img.multiline_text(xy=middle_position, text=text, font=font, stroke_width=2, fill=(255, 255, 255, 255), anchor='mm')
    # image.show()
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
    content.show()

    id = uuid.uuid1()
    save_dir = os.getenv("saved_dir")
    img_name = f"{id}.png"
    img_path = os.path.join(save_dir, img_name)
    content.save(img_path)

    return img_path

make_post_content()