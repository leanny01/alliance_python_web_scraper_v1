import requests
import pprint
from bs4 import BeautifulSoup

response = requests.get('https://www.aljazeera.com/search/covid')

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.select('.gc__title')

for idx, item in enumerate(title):
  print(idx,'. ',item.getText())