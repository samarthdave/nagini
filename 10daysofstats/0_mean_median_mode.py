import collections

def get_median(lst, n):
    lst.sort()
    mid_right = n // 2
    mid_left = mid_right - 1

    if n % 2 == 0:
        return (lst[mid_left] + lst[mid_right]) / 2
    return lst[mid_right]

def get_mode(lst):
    my_hash = collections.defaultdict(int)
    highest_count = 0
    highest_value = None

    for item in lst:
        my_hash[item] += 1
        if my_hash[item] > highest_count:
            highest_count = my_hash[item]
            highest_value = item

    if highest_value == None:
        raise ValueError("No mode exists")

    return highest_value

def main():
    n = int(input())
    lst = list(map(int, input().split(' ')))

    mean_lst   = sum(lst) / n
    median_lst = get_median(lst, n)
    mode_lst   = get_mode(lst)

    print(mean_lst)
    print(median_lst)
    print(mode_lst)

# END MAIN

if __name__ == '__main__':
    main()
