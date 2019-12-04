#!python3
# coding: utf-8

pw_range_min, pw_range_max = 307237, 769058
# pw_range_min, pw_range_max = 307, 358


def check_criteria(number):
    answer = 1
    temp = [c for c in str(number)]
    # Check double numbers
    if len(set(temp)) == len(temp):
        return 0

    # Check left < right
    for j in range(len(temp)-1):
        if int(temp[j]) > int(temp[j + 1]):
            return 0

    # Part 2 code
    # This question is, whether the number has exact 2 double adjacent?
    count_list = [0 for i in range(10)]
    for idx, val in enumerate(temp):
        count_list[int(val)] += 1

    for idx in range(len(count_list)):
        if count_list[idx] == 1:
            count_list[idx] = 0

    minimum = 6
    for idx in range(len(count_list)):
        if count_list[idx] == 0:
            continue

        if count_list[idx] < minimum:
            minimum = count_list[idx]

    if minimum >= 3:
        return 0

    if answer == 1:
        print(number)
    return answer


def solution():
    answer_count = 0
    for i in range(pw_range_min, pw_range_max):
        answer_count += check_criteria(number=i)

    return answer_count


if __name__ == '__main__':
    print(solution())