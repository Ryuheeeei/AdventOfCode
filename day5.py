#!python
# coding: utf-8


def solution():
    with open("data/day5.txt") as f:
        content = f.read().split(",")

    content = [int(num) for num in content]
    idx = 0

    # input_value = 1     # Case 1
    input_value = 5     # Case 2

    while idx < len(content):
        # Read most-right 2 digits
        # First, fill 0 to make code 5 digits
        code = str(content[idx]).zfill(5)
        operator = code[-2:]

        if operator == "99":
            break

        mode_1, mode_2, mode_3 = code[2], code[1], code[0]

        first_parameter = content[idx + 1] if mode_1 == "0" else idx + 1
        second_parameter = content[idx + 2] if mode_2 == "0" else idx + 2
        third_parameter = content[idx + 3] if mode_3 == "0" else idx + 3

        # Add Operator (3 arguments)
        if operator == "01":
            content[third_parameter] = content[first_parameter] + content[second_parameter]
            idx += 4

        # Multiple Operator (3 arguments)
        elif operator == "02":
            content[third_parameter] = content[first_parameter] * content[second_parameter]
            idx += 4

        # Input Operator (1 argument)
        elif operator == "03":
            content[first_parameter] = input_value
            idx += 2

        # Output Operator (1 argument)
        elif operator == "04":
            output_value = content[first_parameter]
            print(output_value)
            idx += 2

        # jump-if-true (2 arguments)
        elif operator == "05":
            if content[first_parameter] != 0:
                idx = content[second_parameter]
            else:
                idx += 3

        # jump-if-false (2 arguments)
        elif operator == "06":
            if content[first_parameter] == 0:
                idx = content[second_parameter]
            else:
                idx += 3

        # less than (3 arguments)
        elif operator == "07":
            content[third_parameter] = 1 if content[first_parameter] < content[second_parameter] else 0
            idx += 4

        # equals (3 arguments)
        elif operator == "08":
            content[third_parameter] = 1 if content[first_parameter] == content[second_parameter] else 0
            idx += 4

        else:
            idx += 1

    return None


if __name__ == '__main__':
    solution()
