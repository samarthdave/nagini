'''
hi! visit the following URL for some context of this script
http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# hold capitals data
# TODO: add feature to map capital to country in linear time
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

source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')

action = ActionChains(driver)
action.drag_and_drop(source, dest).perform()
# alternatively:
# action.click_and_hold(source).pause(1).move_to_element(dest).release(dest).perform()

time.sleep(2)
driver.quit()