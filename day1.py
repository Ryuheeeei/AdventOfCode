#!python
# coding: utf-8

import os


def solution():
    with open("data/day1.txt", "r") as f:
        content = f.read().split("\n")

    answer = 0
    for mass in content:
        answer += int(int(mass) / 3) - 2

    return answer


if __name__ == '__main__':
    result = solution()
    print(result)