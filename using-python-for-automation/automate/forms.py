from selenium import webdriver

driver = webdriver.Chrome()

base_url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(base_url)

# select element, type into & submit
messageField = driver.find_element_by_css_selector('#user-message')
messageField.send_keys('Hello World!')
# get button
messageButton = driver.find_element_by_css_selector('#get-input > button')
messageButton.click()

# sum 2 numbers with 2 inputs lower in the page
sum1_field = driver.find_element_by_css_selector('#sum1')
sum1_field.send_keys('3')
sum2_field = driver.find_element_by_css_selector('#sum2')
sum2_field.send_keys('9')
# press button
compute_sum_btn = driver.find_element_by_css_selector('#gettotal > button')
compute_sum_btn.click()

driver.quit()