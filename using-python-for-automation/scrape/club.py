# use ScrapingClub.com > Exercise 3

# imports
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

# find all cards
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# text properties: name - card-title, price - h5 tag
for block in items:
    itemName  = block.find('h4', class_='card-title').text.strip('\n')
    itemPrice = block.find('h5').text
    print('{} - {}'.format(itemName, itemPrice))