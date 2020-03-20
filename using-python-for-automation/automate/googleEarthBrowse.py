import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# create a webdriver and wait for Google Earth launch button to load
driver = webdriver.Chrome()

base_url = 'https://www.google.com/earth/'
driver.get(base_url)

wait = WebDriverWait(driver, 10)

# wait until the Launch Earth button loads

button_xpath = '/html/body/header/div/nav[1]/ul[2]/li[2]/a'
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

launchEarthButton.click()

# take a look and you'll see into your imagination
time.sleep(3)
driver.quit()