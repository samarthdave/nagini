#!/bin/python3

import math

def cdf(mean, std, x):
    r = (x - mean) / (std * math.sqrt(2))
    res = 0.5 * (1 + math.erf(r))
    # convert to percent
    res *= 100
    return res

if __name__ == '__main__':
    mean, std = map(int, input().split())
    q_1 = float(input())
    q_2 = float(input())

    print(round(100 - cdf(mean, std, q_1), 2))
    print(round(100 - cdf(mean, std, q_2), 2))
    print(round(cdf(mean, std, q_2), 2))
