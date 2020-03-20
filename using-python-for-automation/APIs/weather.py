import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'APPID': '4c576f07b37a8eeef8cb0b885f631015',
    'q': 'New York,US'
}

# api.openweathermap.org/data/2.5/weather?q={city,country}&appid={api_key}
response = requests.get(base_url, params=params)

print(response.content)