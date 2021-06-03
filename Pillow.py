# coding:utf-8

from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os


def scapier():
    search = input("Search for: ")
    parameter = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    request = requests.get('https://www.bing.com/images/search', params=parameter)
    soup = BeautifulSoup(request.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            # Image.open call won't work
            img_obj = requests.get(item.attrs["href"])
            '''
                requests.Session()  .max_redirects = ?
                .headers["location"]
                .headers["User-Agent"]
            '''
            print("Getting ", item.attrs["href"])

            title = item.attrs["href"].split("/")[-1]

            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save('./' + dir_name + '/' + title, img.format)
            except OSError:
                print("Couldn't save image!")
        except ConnectionError:
            print("Couldn't request image!")
        finally:
            scapier()


scapier()
