#!/bin/python3

if __name__ == '__main__':
    a, b = map(float, input().split(" "))

    cost_a = 160 + 40 * (a + a**2)
    cost_b = 128 + 40 * (b + b**2)

    print(round(cost_a, 3))
    print(round(cost_b, 3))
