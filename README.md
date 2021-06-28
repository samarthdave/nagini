# Nagini :snake:

A huge Harry Potter fan myself, I had to give this repository a meaningful name. This is really just doing some ~~Python~~ courses.

## June 2021

[COE 332](https://coe-332-sp21.readthedocs.io)

## August 2020

[Continuing Colt's Course](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass)

[CMU 15-112](https://www.cs.cmu.edu/~112/schedule.html)

## July 2020

[Data Structures & Algo w/ Colt Steele](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass)

## June 2020

[CS50x on edX](https://www.edx.org/course/cs50s-introduction-to-computer-science)

-   just the Python part as a refresher

## May 2020

[Python 3 Bootcamp](https://www.udemy.com/course/the-modern-python3-bootcamp)

[More Web Dev Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp)

#### - implementing Notion's website in Bootstrap

```
# npm install bootstrap & build from source
npm install --save bootstrap
# build with sass (npm install -g sass)
sass --watch main.scss main.css
# and
live-server ./the-web-dev-bootcamp
```

#### - and implementing a static [Yelpcamp](https://yelpcamp-clone.now.sh)

## April 2020

[Colt Steele's Web Dev Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp) - Bootstrap Section

```
# install live-server (node package)
npm install live-server -g

# then run locally for Bootstrap Directory
live-server ./the-web-dev-bootcamp
```

## March 2020

:white_check_mark: [Web Dev Track](https://www.codecademy.com/learn/paths/web-development)

:white_check_mark: [Learn Web Scraping with Beautiful Soup](https://www.codecademy.com/learn/learn-web-scraping)

:white_check_mark: [Automate everything in Python](https://www.linkedin.com/learning/using-python-for-automation)

**libraries/commands used**

```shell
pip3 install beautifulsoup4
pip3 install selenium
```

## July 2019

:white_check_mark: [Get Ready for Your Coding Interview - Lynda](https://www.lynda.com/Software-Development-tutorials/Get-Ready-Your-Coding-Interview)

```python

def find_missing(arr1, arr2):
  # practical approach
  # if 2 inputs are arrays, convert to sets...
  # check if len(arr1) is equal to len(arr2)

  # linear using hash table
  table = dict()

  for item1 in arr2:
    if item1 in table:
      table[item1] += 1
    else:
      table[item1] = 1

  # { 3: 1, 4: 1, }

  # loop thru arr1 & check if i exists in table
    # O(1) - search
  for item2 in arr1:
    # if item does NOT exist, we found our missing
    if item2 not in table:
      return item2

  print("Error, missing item not found")

# print(find_missing([1,2,3], [1,2, 3]))

def find_missing_xor(arr1, arr2):
  xor_sum = 0

  for item1 in arr1:
    xor_sum = xor_sum ^ item1

  for item2 in arr2:
    xor_sum = xor_sum ^ item2

  return xor_sum

# print(find_missing_xor([1,2,3], [1,  3]))

# quarters, dimes, nickels, pennies
# [25, 10, 5, 1]
# num_coins(2) --> 2
def num_coins(cents):
  coin_count = 0

  denominations = [25, 10, 5, 1]
  # quarter, dime ...
  for denom in denominations:
    # the count of coins of this type we can remove
    remove_me = int(cents/denom) # 2/1 --> 2
    cents = cents - (remove_me * denom)

    if remove_me != 0:
      coin_count += remove_me

  return coin_count

# print('31c: ', num_coins(31))
# print(' 2c: ', num_coins(2))
# print('33c: ', num_coins(33))
# 33 --> 1Q, 1N, 3P --> 5

import math
# min_coins(33) --> 4 (inefficient 7) - no Nickels
def min_coins(cents):
  min_coin_count = 0

  denominations = [25, 10, 1]

  extrapolated = []

  for denom in denominations:
    extrapolated.append([])

    max_value = math.ceil(cents/denom) # ceil(33 / 25) = 2
    print(f'denom: {denom}; max: {max_value}')
    for i in range(max_value):
      extrapolated[len(extrapolated) - 1] = denom * (i+1)

  print(extrapolated)

  return min_coin_count

print(min_coins(33))
```
