#!python
# coding: utf-8

import numpy as np

LARGE_NUMBER = 1000000
GRID_SIZE = 20000
central_point_raw = central_point_col = GRID_SIZE // 2
grid = np.zeros(shape=(GRID_SIZE, GRID_SIZE, 2), dtype="int")
shortest_path_count_holder = {}
intersection = []


def find_shortest():
    shortest_path_length = GRID_SIZE * 2
    for point in intersection:
        raw_length = abs(point[0] - central_point_raw)
        col_length = abs(point[1] - central_point_col)
        if raw_length + col_length < shortest_path_length:
            shortest_path_length = raw_length + col_length

    return shortest_path_length


def find_shortest_2():
    shortest_path_length = LARGE_NUMBER
    for point in intersection:
        wire1_length = shortest_path_count_holder[(point[0], point[1], 0)]
        wire2_length = shortest_path_count_holder[(point[0], point[1], 1)]
        if wire1_length + wire2_length < shortest_path_length:
            shortest_path_length = wire1_length + wire2_length

    return shortest_path_length


def check_intersection(now_point, wire_num):
    if wire_num == 0:
        return None

    now_point_raw, now_point_col = now_point[0], now_point[1]
    now_point_value = grid[now_point_raw][now_point_col][0]
    if now_point_value >= 1:
        intersection.append([now_point_raw, now_point_col])
    return None


def write_grid(direction, num, now_point, wire_num, path_count):
    now_point_raw, now_point_col = now_point[0], now_point[1]
    if direction == "R":
        for i in range(num):
            now_point_col += 1
            check_intersection([now_point_raw, now_point_col], wire_num)
            grid[now_point_raw][now_point_col][wire_num] += 1
            path_count += 1
            shortest_path_count_holder.setdefault((now_point_raw, now_point_col, wire_num), path_count)

    elif direction == "U":
        for i in range(num):
            now_point_raw -= 1
            check_intersection([now_point_raw, now_point_col], wire_num)
            grid[now_point_raw][now_point_col][wire_num] += 1
            path_count += 1
            shortest_path_count_holder.setdefault((now_point_raw, now_point_col, wire_num), path_count)

    elif direction == "L":
        for i in range(num):
            now_point_col -= 1
            check_intersection([now_point_raw, now_point_col], wire_num)
            grid[now_point_raw][now_point_col][wire_num] += 1
            path_count += 1
            shortest_path_count_holder.setdefault((now_point_raw, now_point_col, wire_num), path_count)

    elif direction == "D":
        for i in range(num):
            now_point_raw += 1
            check_intersection([now_point_raw, now_point_col], wire_num)
            grid[now_point_raw][now_point_col][wire_num] += 1
            path_count += 1
            shortest_path_count_holder.setdefault((now_point_raw, now_point_col, wire_num), path_count)

    return [now_point_raw, now_point_col], path_count


def solution():
    with open("./data/day3.txt", "r") as f:
        wire1 = f.readline().split(",")
        wire2 = f.readline().split(",")

    now_point_raw, now_point_col = central_point_raw, central_point_col
    now_point = [now_point_raw, now_point_col]
    shortest_path_count_holder.setdefault((now_point_raw, now_point_col, 0), 0)
    path_count = 0

    for command in wire1:
        direction = command[0]
        num = int(command[1:])
        now_point, path_count = write_grid(direction, num, now_point, 0, path_count)

    grid[now_point_raw][now_point_col][0] += 1
    shortest_path_count_holder.setdefault((now_point_raw, now_point_col, 0), path_count)

    path_count = 0
    now_point = [central_point_raw, central_point_col]
    for command in wire2:
        direction = command[0]
        num = int(command[1:])
        now_point, path_count = write_grid(direction, num, now_point, 1, path_count)

    answer = find_shortest_2()
    return answer


if __name__ == '__main__':
    print(solution())
