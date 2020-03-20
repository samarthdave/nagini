'''
hi! visit the following URL for some context of this script
http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# hold capitals data
# TODO: [x] add feature to map capital to country in linear time
country_capitals = {
    'Oslo': 'Norway',
    'Stockholm': 'Sweden',
    'Washington': 'United States',
    'Copenhagen': 'Denmark',
    'Seoul': 'South Korea',
    'Rome': 'Italy',
    'Madrid': 'Spain'
}

# do the browser things:
driver = webdriver.Chrome()
driver.maximize_window()

base_url = 'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver.get(base_url)

# utility function for generating xpath
build_xpath_by_id = lambda a: '//*[@id="{}"]'.format(a)

# get capitals on the left
capitals_holder = driver.find_element_by_css_selector('#capitals > #dropContent')
capital_boxes = capitals_holder.find_elements_by_css_selector("*")
# get all city boxes and assign city with xpath
# eg. { 'Norway': '//*[@id=box4]', ... }
city_id_values = {}
for item in capital_boxes:
    city_name = item.text.strip()
    # if valid city, print it and add to list
    if len(city_name) > 0:
        print('--' + city_name + '--')
        city_id_values[city_name] = build_xpath_by_id(item.get_attribute('id'))

print(city_id_values)

print('=======================')

# get all countries on the left
countries_holder = driver.find_element_by_css_selector('#countries')
country_boxes = countries_holder.find_elements_by_css_selector("*")

country_id_values = {}
for item in country_boxes:
    country_name = item.text.strip()
    # if valid country, print it and add to list
    if len(country_name) > 0:
        print('--' + country_name + '--')
        country_id_values[country_name] = build_xpath_by_id(item.get_attribute('id'))

print(country_id_values)

# get all country boxes and assign with xpath
# eg. { 'Norway': '//*[@id=box4]', ... }

action = ActionChains(driver)

# loop thru every key/value pair
for capital, country in country_capitals.items():
    # if both values exist in dictionary, then drag and drop w/ dictionaries
    if (capital in city_id_values) and (country in country_id_values):
        # dictionaries store the xpaths of both
        source = driver.find_element_by_xpath(city_id_values[capital])
        dest = driver.find_element_by_xpath(country_id_values[country])
        # drag and drop it over (faster than .drag_and_drop)
        action.click_and_hold(source).pause(0.1).move_to_element(dest).release(dest).perform()
        # alternatively
        # action.drag_and_drop(source, dest).perform()

time.sleep(2)
driver.quit()