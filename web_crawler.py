# coding: utf-8
#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import operator
from collections import Counter


def spider(url):
    wordlist = []
    target = requests.get(url).text
    soup = BeautifulSoup(target, 'html.parser')

    for element in soup.findAll('div', {'class': 'entry-content'}):
        content = element.text
        words = content.lower().split()

        for word in words:
            wordlist.append(word)

        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\\;:"<>?/., '

        for index in range(0, len(symbols)):
            word = word.replace(symbols[index], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print('%s : %s' % (key, value))

    total = Counter(word_count)
    top = total.most_common(10)

    print(top)


if __name__ == '__main__':
    spider(
        'https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar'
    )
