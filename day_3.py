import re

if __name__ == '__main__':
    result_one = 0
    result_two = 0
    enabled = True
    print("Paste your input here (end input with empty line):")
    while True:
        t = input()
        if t == '': break

        for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", t):
            if match == "don't()":
                enabled = False
            elif match == "do()":
                enabled = True
            else:
                result_one += (int(match[4:match.find(',')]) * int(match[match.find(',') + 1:-1]))
                if enabled:
                    result_two += (int(match[4:match.find(',')]) * int(match[match.find(',') + 1:-1]))

    print(f"Part one: {result_one}")
    print(f"Part two: {result_two}")
