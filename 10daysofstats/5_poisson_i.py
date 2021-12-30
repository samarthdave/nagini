#!/bin/python3

def fact(n):
    if n <= 0: return 1
    result = 1
    for i in range(1, n+1):   
        result *= i
    return result

e = 2.7182818284590

# k & lambda
def poisson(k, l):
    return (l**k) * (e**(-l)) / fact(k)

if __name__ == '__main__':
    mean = float(input())

    X = int(input())
    print(round(poisson(X, mean), 3))
