import requests
from PIL import Image


def convert(url_img, url_save_img, to_format):
    im = Image.open(url_img).convert("RGB")
    im.save(url_save_img, to_format)


def getImgFromWeb(img_url, img_name):
    response = requests.get(img_url)
    with open(img_name, 'wb') as file:
        file.write(response.content)
