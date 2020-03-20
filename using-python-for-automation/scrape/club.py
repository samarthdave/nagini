# use ScrapingClub.com > Exercise 3

# imports
import requests
from bs4 import BeautifulSoup

base_url = 'https://scrapingclub.com/exercise/list_basic/'
resp = requests.get(base_url)
soup = BeautifulSoup(resp.text, 'lxml')

# find all cards
count = 0
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# text properties: name - card-title, price - h5 tag
for block in items:
    count += 1
    itemName  = block.find('h4', class_='card-title').text.strip('\n')
    itemPrice = block.find('h5').text
    print('{0}: {1:<30} - {2}'.format(count, itemName, itemPrice))

# PAGINATION
# hold all urls (prev, 1, 2, ... 5, next)
page_refs = soup.find('ul', class_='pagination')
# append to these arrays with .../...?page=N
urls = []
full_urls = []
# get all anchor tags
links = page_refs.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    # if not None (since None is "falsey")
    if pageNum:
        x = link.get('href')
        urls.append(x)
        full_urls.append(base_url + x)

# print all hrefs
print('='*20)
for i in full_urls:
    print(i)
print('='*20)

# ask user if should paginate through all URLs
prompt_resp = input("Explore the above URLs found in pagination (yes/no)? ")
should_explore = prompt_resp.lower() == 'yes'

# convert all to real urls from base url
for url in full_urls:
    # if shouldn't make request to all paths then break
    if not should_explore:
        break
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    # find all cards
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    # text properties: name - card-title, price - h5 tag
    for block in items:
        count += 1
        itemName  = block.find('h4', class_='card-title').text.strip('\n')
        itemPrice = block.find('h5').text
        print('{0}: {1:<30} - {2}'.format(count, itemName, itemPrice))