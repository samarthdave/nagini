#!/bin/python3

# helpful link for understanding the normal distribution
# https://onlinestatbook.com/2/calculators/normal_dist.html

import math

def cdf(mean, std, x):
    r = (x - mean) / (std * (2 ** 0.5))
    res = 0.5 * (1 + math.erf(r))
    return res

if __name__ == '__main__':
    mean, std = map(int, input().split())
    n = float(input())
    range_a, range_b = map(int, input().split())

    print(round(cdf(mean, std, n), 3))
    print(round(cdf(mean, std, range_b) - cdf(mean, std, range_a), 3))
