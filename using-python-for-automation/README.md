# [Automate everything in Python :snake:](https://www.linkedin.com/learning/using-python-for-automation/)

### Directories
```
automate - browser automation w/ Selenium
io       - read and write to files w/o modules
organize - work with directories/folders to organize files
scrape   - web scraping & handling pagination
terminal - interact with terminal (using subprocess)
```

#### what I learned
- the barcode API is open
**https://api.upcitemdb.com/prod/trial/lookup?upc=12993401085**

- selenium is inconsiswtent
```
These functions are janky and some work better than others
# find_element_by_id
# find_element_by_xpath
# find_element_by_css_selector
```

- selenium is still easy to code in, case in point:
```python
action = ActionChains(driver)
action.drag_and_drop(source, dest).perform()
```

Relevant links & references
- http://quotes.toscrape.com/
- https://scrapingclub.com/exercise/list_basic/
- https://www.seleniumeasy.com/test/basic-first-form-demo.html
- http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html