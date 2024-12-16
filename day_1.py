first = []
second = []
print("Paste your input here (end input with empty line):")
while True:
    t = input()
    if t != '':
        t = t.split(' ')
        first.append(int(t[0]))
        second.append(int(t[-1]))
    else:
        break

print(f"Part one: {sum([abs(f - s) for f, s in zip(sorted(first), sorted(second))])}")
print(f"Part two: {sum([number * second.count(number) for number in first])}")