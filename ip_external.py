import re
import json
import codecs
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
reader = codecs.getreader('utf-8')
response = urlopen(url)
data = json.load(reader(response))
ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('External IP details')
print(
    'Organization: {4}\nCountry: {3}\nRegion: {2}\nCity: {1}\nIP: {0}'.format(
        ip, city, region, country, org))
