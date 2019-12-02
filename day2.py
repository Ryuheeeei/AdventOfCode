#!python
# coding: utf-8

ANSWER_CONSTANT = 19690720


def solution(noun, verb):
    with open("data/day2.txt") as f:
        content = f.read().split(",")

    content = [int(num) for num in content]
    skip_count = 0

    # For Case 1, noun = 12, verb = 2
    content[1] = noun
    content[2] = verb

    for idx, code in enumerate(content):
        if skip_count > 0:
            skip_count -= 1
            continue

        if code == 1:
            content[content[idx + 3]] = content[content[idx + 2]] + content[content[idx + 1]]
            skip_count = 3
        elif code == 2:
            content[content[idx + 3]] = content[content[idx + 2]] * content[content[idx + 1]]
            skip_count = 3
        elif code == 99:
            break

    return content[0]


if __name__ == '__main__':
    for noun in range(100):
        for verb in range(100):
            if solution(noun, verb) == ANSWER_CONSTANT:
                print("noun: {}, verb: {}, 100 * noun + verb :{}".
                      format(noun, verb, 100 * noun + verb))
