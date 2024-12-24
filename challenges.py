import re
import itertools


def get_input() -> list:
    whole_input = []
    while True:
        t = input()
        if t == '': break

        whole_input.append(t)

    return whole_input


def day_1() -> (int, int):
    first = []
    second = []
    print("Paste your input here (end input with an empty line):")
    input_lines = get_input()
    for line in input_lines:
        line = line.split(' ')
        first.append(int(line[0]))
        second.append(int(line[-1]))

    return (sum([abs(f - s) for f, s in zip(sorted(first), sorted(second))]),
            sum([number * second.count(number) for number in first]))


def day_2() -> (int, int):
    def is_safe(_report: list, tolerate_single_bad_level: bool) -> bool:
        if tolerate_single_bad_level:
            for i in range(len(_report)):
                t = _report[:i] + _report[i + 1:]
                if all([(t == sorted(t) or t == sorted(t, reverse=True)),
                        (min([abs(x - y) for x, y in zip(t, t[1:])]) >= 1),
                        (max([abs(x - y) for x, y in zip(t, t[1:])]) <= 3)]):
                    return True
            return False
        else:
            return all([(_report == sorted(_report) or _report == sorted(_report, reverse=True)),
                        (min([abs(x - y) for x, y in zip(_report, _report[1:])]) >= 1),
                        (max([abs(x - y) for x, y in zip(_report, _report[1:])]) <= 3)])

    reports = []
    print("Paste your input here (end input with an empty line):")
    input_lines = get_input()
    for line in input_lines:
        reports.append([int(x) for x in line.split(' ')])

    return (len([report for report in reports if is_safe(report, False)]),
            len([report for report in reports if is_safe(report, True)]))


def day_3() -> (int, int):
    result_one = 0
    result_two = 0
    enabled = True
    print("Paste your input here (end input with an empty line):")
    input_lines = get_input()
    for line in input_lines:
        for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line):
            if match == "don't()":
                enabled = False
            elif match == "do()":
                enabled = True
            else:
                result_one += (int(match[4:match.find(',')]) * int(match[match.find(',') + 1:-1]))
                if enabled:
                    result_two += (int(match[4:match.find(',')]) * int(match[match.find(',') + 1:-1]))

    return result_one, result_two


def day_4() -> (int, int):
    xmas_count = 0
    x_mas_count = 0
    print("Paste your input here (end input with an empty line):")
    input_lines = get_input()
    columns_count = len(input_lines[0])
    rows_count = len(input_lines)
    for i in range(rows_count):
        for j in range(columns_count):
            if input_lines[i][j] == 'X':
                for i_step, j_step in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
                    for c in range(1, 4):
                        next_i = i + i_step * c
                        next_j = j + j_step * c
                        if not ((0 <= next_i < rows_count) and (0 <= next_j < columns_count)):
                            break
                        elif input_lines[next_i][next_j] != 'XMAS'[c]:
                            break
                        elif c == 3:
                            xmas_count += 1
            if all([(input_lines[i][j] == 'A'), (0 <= i + 1 < rows_count), (0 <= i - 1 < rows_count),
                    (0 <= j + 1 < columns_count), (0 <= j - 1 < columns_count)]):
                if (input_lines[i-1][j-1] + input_lines[i+1][j+1] in ['MS', 'SM']) and (input_lines[i-1][j+1] + input_lines[i+1][j-1] in ['MS', 'SM']):
                    x_mas_count += 1

    return xmas_count, x_mas_count


def day_5() -> (int, int):
    rules = []
    updates = []
    correct_middle_sum = 0
    incorrect_middle_sum = 0
    print("Paste your input here (end input with an empty line):")
    input_lines = get_input()
    for line in input_lines:
        line = line.split('|')
        rules.append((line[0], line[1]))
    input_lines = get_input()
    for line in input_lines:
        updates.append(line.split(','))

    for update in updates:
        correct = True
        applying_rules = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                applying_rules.append(rule)
                if update.index(rule[0]) > update.index(rule[1]):
                    correct = False
        if correct:
            correct_middle_sum += int(update[int(len(update)/2)])
        else:
            while not correct:
                correct = True
                for rule in applying_rules:
                    if update.index(rule[0]) > update.index(rule[1]):
                        correct = False
                        t = rule[1]
                        update.remove(t)
                        update.append(t)
            incorrect_middle_sum += int(update[int(len(update)/2)])

    return correct_middle_sum, incorrect_middle_sum


def day_6() -> (int, int):
    print("Paste your input here (end input with an empty line):")
    input_lines = [list(line) for line in get_input()]

    columns_count = len(input_lines[0])
    rows_count = len(input_lines)
    directions = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    marker = '^'
    joined = ''.join([''.join(line) for line in input_lines])
    starting = (joined.index(marker)//columns_count, joined.index(marker)%columns_count)

    current_y, current_x = starting
    next_y, next_x = current_y + directions[marker][0], current_x + directions[marker][1]
    visited_positions = set()
    while (0 <= next_y < rows_count) and (0 <= next_x < columns_count):
        if input_lines[next_y][next_x] == '#':
            marker = list(directions.keys())[(list(directions.keys()).index(marker)+1)%4]
            next_y, next_x = current_y + directions[marker][0], current_x + directions[marker][1]
        else:
            visited_positions.add((current_y, current_x))
            current_y, current_x, next_y, next_x = next_y, next_x, next_y + directions[marker][0], next_x + directions[marker][1]
    visited_positions.add((current_y, current_x))
    positions_counter = len(visited_positions)

    possible_obstacles_counter = 0
    visited_positions.remove(starting)
    for position in visited_positions:
        temp_visited = set()
        input_lines[position[0]][position[1]] = '#'
        marker = '^'
        current_y, current_x = starting
        next_y, next_x = current_y + directions[marker][0], current_x + directions[marker][1]
        while (0 <= next_y < rows_count) and (0 <= next_x < columns_count):
            if input_lines[next_y][next_x] == '#':
                marker = list(directions.keys())[(list(directions.keys()).index(marker) + 1) % 4]
                next_y, next_x = current_y + directions[marker][0], current_x + directions[marker][1]
            else:
                if (current_y, current_x, marker) in temp_visited:
                    possible_obstacles_counter += 1
                    break
                temp_visited.add((current_y, current_x, marker))
                current_y, current_x, next_y, next_x = next_y, next_x, next_y + directions[marker][0], next_x + directions[marker][1]
        input_lines[position[0]][position[1]] = '.'

    return positions_counter, possible_obstacles_counter


def day_7() -> (int, int):
    print("Paste your input here (end input with an empty line):")
    input_lines = [line.replace(':','').split(' ') for line in get_input()]
    total_calibration_result = 0
    with_concatenation = 0
    for equation in input_lines:
        to_eval = None
        for operators in itertools.product(['+', '*'], repeat=(len(equation)-2)):
            to_eval = "("*len(operators) + equation[1]
            for operator, number in zip(operators, equation[2:]):
                to_eval += f"{operator}{number})"
            to_eval = eval(to_eval)
            if to_eval == int(equation[0]):
                total_calibration_result += to_eval
                break
        if not to_eval == int(equation[0]):
            for operators in [combination for combination in itertools.product(['||', '+', '*'], repeat=(len(equation) - 2)) if '||' in combination]:
                to_eval = equation[1]
                for operator, number in zip(operators, equation[2:]):
                    match operator:
                        case '+':
                            to_eval = str(int(to_eval) + int(number))
                        case '*':
                            to_eval = str(int(to_eval) * int(number))
                        case '||':
                            to_eval += number
                        case _:
                            raise SyntaxError

                if to_eval == equation[0]:
                    with_concatenation += int(to_eval)
                    break

    return total_calibration_result, (total_calibration_result+with_concatenation)


def day_8() -> (int, int):
    return 0, 0


def day_9() -> (int, int):
    return 0, 0


def day_10() -> (int, int):
    return 0, 0


def day_11() -> (int, int):
    return 0, 0


def day_12() -> (int, int):
    return 0, 0


def day_13() -> (int, int):
    return 0, 0


def day_14() -> (int, int):
    return 0, 0


def day_15() -> (int, int):
    return 0, 0


def day_16() -> (int, int):
    return 0, 0


def day_17() -> (int, int):
    return 0, 0


def day_18() -> (int, int):
    return 0, 0


def day_19() -> (int, int):
    return 0, 0


def day_20() -> (int, int):
    return 0, 0


def day_21() -> (int, int):
    return 0, 0


def day_22() -> (int, int):
    return 0, 0


def day_23() -> (int, int):
    return 0, 0


def day_24() -> (int, int):
    return 0, 0


def day_25() -> (int, int):
    return 0, 0
