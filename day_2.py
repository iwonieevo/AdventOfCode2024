def is_safe(_report: list) -> bool:
    for i in range(len(_report)):
        t = _report[:i] + _report[i + 1:]
        if all([(t == sorted(t) or t == sorted(t, reverse=True)),
                (min([abs(x - y) for x, y in zip(t, t[1:])]) >= 1),
                (max([abs(x - y) for x, y in zip(t, t[1:])]) <= 3)]):
            return True
    return False

if __name__ == '__main__':
    reports = []
    print("Paste your input here (end input with empty line):")
    while True:
        t = input()
        if t == '': break

        reports.append([int(x) for x in t.split(' ')])

    print(f"Part one: {len([report for report in reports
          if (report == sorted(report) or report == sorted(report, reverse=True))
             and (min([abs(x - y) for x, y in zip(report, report[1:])]) >= 1)
             and (max([abs(x - y) for x, y in zip(report, report[1:])]) <= 3)])}")

    print(f"Part two: {len([report for report in reports if is_safe(report)])}")
