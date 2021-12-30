#!/bin/python3

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    numerator = 0
    denominator = sum(W)

    count = len(X)
    if len(X) != len(W): raise ValueError("Invalid inputs, X and W should be same length")
    for i in range(count):
        numerator += (X[i] * W[i])

    print(round(numerator / denominator, 1))

def main():
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)

if __name__ == '__main__':
    main()
