#!python
# coding: utf-8

import os


def solution():
    with open("data/day1_2.txt", "r") as f:
        content = f.read().split("\n")

    answer = 0
    for mass in content:
        temp = int(mass)
        while temp / 3 > 0:
            answer += max(int(temp / 3) - 2, 0)
            temp = int(temp / 3) - 2

    return answer


if __name__ == '__main__':
    result = solution()
    print(result)