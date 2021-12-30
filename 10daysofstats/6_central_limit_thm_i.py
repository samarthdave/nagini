import math

def cdf(mean, std, x):
    Z = (x - mean) / std
    r = Z / math.sqrt(2)
    return (1 + math.erf(r)) / 2

if __name__ == '__main__':
    x = float(input())
    n = float(input())
    mean = float(input())
    sigma = float(input())

    mu = n * mean 
    sigma = math.sqrt(n) * sigma

    print(round(cdf(mu, sigma, x), 4))
