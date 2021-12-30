#!/bin/python3

def fact(n):
    if n <= 0: return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def comb(n, k):
    if k > n: return 0
    return fact(n) / (fact(k) * fact(n - k))
def binom(x, n, p):
    res = comb(n, x) * (p**x) * ((1-p)**(n-x))
    return res

if __name__ == '__main__':
    p, n = list(map(int, input().split(" ")))
    p = float(p/100)

    # question 1
    part_a = sum([binom(i, n, p) for i in range(0, 3)])
    print(round(part_a, 3))

    # question 2
    # P(X>=2) = 1 - P(X<2)
    part_b = 1 - binom(0, n, p) - binom(1, n, p)
    print(round(part_b, 3))
