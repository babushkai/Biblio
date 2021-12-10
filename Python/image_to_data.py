import os 
from io import BytesIO
import requests
from PIL import Image
import sys

def data_to_img(data):
    """Return PIL Image object, with data from in-memory <data>"""
    fp = BytesIO(data)
    return Image.open(fp)    # reads from memory

def img_to_data(img, fmt=None):
    """Return image data from PIL Image <img>, in <fmt> format"""
    fp = BytesIO()
    if not fmt:
        fmt = img.format     # keeps the original format
    img.save(fp, fmt)        # writes to memory
    return fp.getvalue()

def convert_image(data, fmt=None):
    """Convert image <data> to PIL <fmt> image data"""
    img = data_to_img(data)
    return img_to_data(img, fmt)

def get_file_data(name):
    """Return PIL Image object for image file <name>"""
    img = Image.open(name)
    print("img", img, img.format)
    return img_to_data(img)

if __name__ == "__main__":
    lnk = "https://media.vanityfair.com/photos/5bbf71bf11e2562d6f9da574/9:16/w_629,h_1119,c_limit/scarlett-johansson-black-widow-15-million.jpg"
    img = requests.get(lnk, stream=True).raw
    data = get_file_data(img)
    print("in", len(data), data[:10])
    for fmt in ("gif", "png", "jpeg"):
        out_data = convert_image(data, fmt)
        print("out", len(out_data), out_data[:10])
    