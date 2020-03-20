import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# parse the html w/ beautifulsoup & lxml
soup = BeautifulSoup(response.text, 'lxml')

quotes  = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags    = soup.find_all('div', class_='tags')

# print out all quote, author and tags
for i in range(len(quotes)):
    print('{} - {}'.format(quotes[i].text, authors[i].text))
    # get all category/tag values
    quoteTags = tags[i].find_all('a', class_='tag')
    print('[ ', end='')
    for quote in quoteTags:
        print(quote.text, end=' ')
    print(']')