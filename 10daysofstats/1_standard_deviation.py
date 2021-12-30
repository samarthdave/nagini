#!/bin/python3

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    n = len(arr)

    mean = sum(arr) / n
    variance = sum([(x - mean) ** 2 for x in arr]) / n
    st_dev = variance ** 0.5

    print("{0:0.1f}".format(st_dev))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
