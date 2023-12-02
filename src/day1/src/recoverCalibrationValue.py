def recoverCalibrationValuesPart1(inputLines):
    # Alternate Solution
    # for line in inputLines:
    #     x = 0
    #     y = 0
    #     for l in list(line):
    #         if l.isdigit():
    #             x = int(l)
    #             break
    #
    #     for l in list(line[::-1]):
    #         if l.isdigit():
    #             y = int(l)
    #             break
    #     sum+=x*10+y
    sum = 0
    for line in inputLines:
        num = [int(n) for n in list(line) if n.isdigit()]
        sum += num[0]*10 + num[-1]

    return sum

def find_real_int(line, get_first = True):
    valid_spelled_int = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    valid_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dict_spelled_int = {}
    dict_int = {}

    for i, v in enumerate(valid_spelled_int):
        if get_first:
            dict_spelled_int[line.find(v)] = i+1
        elif line.find(v)!= -1:
            dict_spelled_int[line.rindex(v)] = i+1
        else:
            dict_spelled_int[-1] = i+1
    del dict_spelled_int[-1]

    for v in valid_int:
        if get_first:
            dict_int[line.find(str(v))] = v
        elif line.find(str(v)) != -1:
            dict_int[line.rindex(str(v))] = v
        else:
            dict_int[-1] = v
    del dict_int[-1]

    if len(dict_spelled_int) != 0 and len(dict_int) != 0:
        if get_first:
            min_index_spelled_int = min(dict_spelled_int.keys())
            min_index_int = min(dict_int.keys())

            return dict_spelled_int[min_index_spelled_int] if min_index_spelled_int < min_index_int else dict_int[min_index_int]
        else:
            max_index_spelled_int = max(dict_spelled_int.keys())
            max_index_int = max(dict_int.keys())

            return dict_spelled_int[max_index_spelled_int] if max_index_spelled_int > max_index_int else dict_int[max_index_int]

    elif len(dict_spelled_int) != 0 and len(dict_int) == 0:
        if get_first:
            return dict_spelled_int[min(dict_spelled_int.keys())]
        else:
            return dict_spelled_int[max(dict_spelled_int.keys())]

    else:
        if get_first:
            return dict_int[min(dict_int.keys())]
        else:
            return dict_int[max(dict_int.keys())]


def recoverCalibrationValuesPart2(inputLines):
    sum = 0
    for line in inputLines:
        first = find_real_int(line)
        second = find_real_int(line, False)
        sum += first*10 + second

    return sum

if __name__ == "__main__":
    input = open(r"day1.txt")
    sumOfCalibratedValues = recoverCalibrationValuesPart1(input.readlines())
    input.close()

    input = open(r"day1.txt")
    correctedSumOfCalibratedValues = recoverCalibrationValuesPart2(input.readlines())
    input.close()

    print("Day 1:")
    print("\tPart 1: ", sumOfCalibratedValues)
    print("\tPart 2: ", correctedSumOfCalibratedValues)
