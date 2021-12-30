#!/bin/python3

# visualize negative binomial distribution
# https://www.desmos.com/calculator/uofurqtptg

def geom(n, p):
    q = 1 - p
    res = q**(n-1) * p
    return res

if __name__ == '__main__':
    a, b = list(map(int, input().split(" ")))
    p = a / b
    n = int(input())

    print(round(1 - (1-p)**(n), 3))
