import textwrap
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters

quote = "I can write on images with Python now and I like it!"
font = ImageFont.truetype(font=r"C:\Windows\Fonts\Arial.ttf", size=60)
avg_char_width = sum(font.getlength(char) for char in ascii_letters) / len(ascii_letters)

with Image.open(r"C:\Users\mikol\Documents\Q1Y3\4GC00\MTS.png") as img:
    max_char_count = int((img.size[0] * .95) / avg_char_width)
    text = textwrap.fill(text=quote, width=max_char_count)
    print(text)
    I1 = ImageDraw.Draw(img)
    I1.multiline_text(xy=(img.size[0]/2, img.size[1] / 2), text=text, font=font, fill='#000000', anchor='mm')
    img.show()
    # img.save("image.png")


