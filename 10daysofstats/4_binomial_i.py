#!/bin/python3

# iterative factorial implementation
def fact(n):
    if n <= 0: return 1

    result = 1
    for i in range(1, n+1):
        result *= i

    return result

# n choose k = n!/(k! * (n-k)!)
def comb(n, k):
    if k > n: return 0
    return fact(n) / (fact(k) * fact(n - k))

def binom(x, n, p):
    res = comb(n, x) * (p**x) * ((1-p)**(n-x))
    return res

if __name__ == '__main__':
    # 1.09 1
    a, b = list(map(float, input().split()))

    p = float(a/(a+b))
    _n = 6 # six children

    total = 0
    for i in range(3, 6+1): # 6 total, range is exclusive
        total += binom(i, _n, p)

    print(round(total, 3))
