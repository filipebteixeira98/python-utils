#coding: utf-8
#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

target = requests.get('https://www.google.com').content
soup = BeautifulSoup(target, 'html.parser')
search = soup.find('b', class_="gb1")

# print(soup.prettify())
# print(soup.title)
# print(soup.a) Retrieve from HTML tags
# print(soup.p)
print(search.string)