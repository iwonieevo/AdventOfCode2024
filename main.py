from challenges import *


if __name__ == '__main__':
    funcs = {
        '1': day_1,
        '2': day_2,
        '3': day_3,
        '4': day_4,
        '5': day_5,
        '6': day_6,
        '7': day_7,
        '8': day_8,
        '9': day_9,
        '10': day_10,
        '11': day_11,
        '12': day_12,
        '13': day_13,
        '14': day_14,
        '15': day_15,
        '16': day_16,
        '17': day_17,
        '18': day_18,
        '19': day_19,
        '20': day_20,
        '21': day_21,
        '22': day_22,
        '23': day_23,
        '24': day_24,
        '25': day_25
    }
    func = funcs.get(input("Input which day challenge would you like to get answers to (input a day number): "), None)
    if func is None:
        print(f"Incorrect input! Possible options are: {', '.join(list(funcs.keys()))}")
    else:
        answers = func()
        print(f"Part one: {answers[0]}")
        print(f"Part two: {answers[1]}")
