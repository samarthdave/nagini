#!/bin/python3

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def split_arr(arr):
    n = len(arr)
    middle = n // 2
    if n % 2 == 0:
        return arr[0:middle], arr[middle:]
    else:
        # if odd, exclude middle item
        # note, Python list slicing is exclusive on endpoint
        return arr[0:middle], arr[middle + 1:]

def get_median(lst, avoid_sort=False):
    if not avoid_sort:
        lst.sort()

    n = len(lst)
    mid_right = n // 2

    if n % 2 == 0:
        mid_left = mid_right - 1
        return int((lst[mid_left] + lst[mid_right]) / 2)

    return int(lst[mid_right])

def quartiles(arr):
    # Write your code here
    arr.sort()

    left_arr, right_arr = split_arr(arr)

    q_1 = get_median(left_arr, avoid_sort=True)
    q_2 = get_median(arr, avoid_sort=True)
    q_3 = get_median(right_arr, avoid_sort=True)
    return [q_1, q_2, q_3]

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    combined = list(zip(values, freqs))
    combined.sort(key=lambda x: x[0])

    arr = []
    for pair in combined:
        curr = [pair[0]] * pair[1]
        arr += curr

    lst = quartiles(arr)
    print(float(lst[2] - lst[0]))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)
