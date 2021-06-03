# coding:utf-8

from bs4 import BeautifulSoup
import requests


def scrapier():
    search = input("Search for: ")
    parameter = {"q": search}
    request = requests.get('https://www.bing.com/search', params=parameter)

    soup = BeautifulSoup(request.text, "html.parser")
    result = soup.find("ol", {"id": "b_results"})
    links = result.findAll("li", {"class": "b_algo"})

    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            print(item_text)
            print(item_href)
            print(item.find("a").parent.parent.parent.find("p").text)
        '''
            children = item.children
            for child in children:
                print(child)
                print(child.next_sibling)
        '''


scrapier()
