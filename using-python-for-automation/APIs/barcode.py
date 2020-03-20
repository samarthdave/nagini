import requests
import json

base_url = 'https://api.upcitemdb.com/prod/trial/lookup'
# .../lookup?upc=...
item_query_string = 'upc'
# can you tell what my favorite flavor is?
la_croix_lime = '12993401085'

# get input from terminal
query = input('Enter a UPC (enter for default): ')
final_upc = la_croix_lime if query == "" else query

params = { item_query_string: final_upc }

response = requests.get(base_url, params=params)
print(response.url)

content = response.content
info = json.loads(content)

print('==============================')
# access items array
product_info  = info['items'][0]
product_brand = product_info['brand']
product_title = product_info['title']
print('{0:>10} - {1}'.format(product_brand, product_title))

# print all offers
offers = product_info['offers']
for offer in offers:
    print('\tBuy @ {} for ${} + shipping(${})'.format(offer['merchant'], offer['price'], offer['shipping']))

print('==============================')