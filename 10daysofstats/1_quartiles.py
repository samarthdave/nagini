#!/bin/python3

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def split_arr(arr):
    n = len(arr)
    middle = n // 2
    # n = 4 vs n = 5
    # [12, 32,     65, 83] --> split --> [12, 32], [65, 83]
    # [12, 32, 46, 65, 83] --> split --> [12, 32], [65, 83]

    if n % 2 == 0:
        return arr[:middle], arr[middle:]
    else:
        # if odd, exclude "middle" item
        # note, python list slicing is exclusive on endpoint
        return arr[:middle], arr[middle + 1:]

def get_median(lst):
    n = len(lst)
    lst.sort()
    mid_right = n // 2
    mid_left = mid_right - 1

    if n % 2 == 0:
        return (lst[mid_left] + lst[mid_right]) / 2
    return lst[mid_right]

def quartiles(arr):
    # Write your code here
    arr.sort()

    left_arr, right_arr = split_arr(arr)

    # casting to an int so hackerrank accepts
    q_1 = int(get_median(left_arr))
    # Q2 is the same as median of the whole thing
    q_2 = int(get_median(arr))
    q_3 = int(get_median(right_arr))
    return [q_1, q_2, q_3]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
