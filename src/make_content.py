import textwrap
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters


def connect_quotes_api():
    """ Connect to Quotes API.

    Raises
    ------
    Exception as e
        If could not initialize Quotes API connection.

    Returns
    --------
    some.api.API
        Connected API object
    """

    api = "some api"
    return api


def connect_images_api():
    """ Connect to images API.

    Raises
    ------
    Exception as e
        If could not initialize images API connection.

    Returns
    --------
    some.api.API
        Connected API object
    """
    api = "some api"
    return api


def get_quote(api_quotes):
    """ GET random quote from Quotes API.

    Returns
    -------
    quote: str
        string fetched from Quotes API
    """

    quote = "I can write on images with Python now and I like it!"
    return quote


def get_background_img(api_images):
    """ Get random background image from Images API.

    Returns
    -------
    image: PIL.PngImagePlugin.PngImageFile
        image fetched from images API
    """

    image = r"C:\Users\mikol\Documents\Q1Y3\4GC00\MTS.png"
    return image


def write_quote_on_image(quote: str, image: str):
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

    font = ImageFont.truetype(font=r"C:\Windows\Fonts\Arial.ttf", size=60)
    avg_char_width = sum(font.getlength(char) for char in ascii_letters) / len(ascii_letters)

    with Image.open(image) as img:
        max_char_count = int((img.size[0] * .95) / avg_char_width)
        text = textwrap.fill(text=quote, width=max_char_count)
        I1 = ImageDraw.Draw(img)
        I1.multiline_text(xy=(img.size[0]/2, img.size[1] / 2), text=text, font=font, fill='#000000', anchor='mm')
        img.show()
        # img.save("image.png")
        return img


def make_post_content(api_quotes, api_images):
    """ Create a new instance of image with quote to be tweeted.

    Parameters
    ----------
    api_quotes : some.api.API
        The tweepy quotes API object
    api_images : some.api.API
        The tweepy quotes API object

    Returns
    ------
    content: PIL.PngImagePlugin.PngImageFile
        Image with quote of .png format
    """

    quote = get_quote(api_quotes)
    image = get_background_img(api_images)
    content = write_quote_on_image(quote, image)
    return content
