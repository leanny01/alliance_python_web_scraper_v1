# request, pprint, Beautifulsoup
# https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
import requests
import pprint
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')


# print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
links = soup.select('.titlelink')
subtexts = soup.select('.subtext')

def create_custom_news(links, subtexts):
  news = []

  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href')
    points = subtexts[idx].select('.score')

    news.append({'title':title, 'link':href,'votes':points})
  
  pprint.pprint(news)


create_custom_news(links, subtexts)