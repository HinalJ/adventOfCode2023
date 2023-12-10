def extrapolate_value_from_history_end(history):
    new_hist = []
    all_zeroes = True
    for i in range(1, len(history)):
        new_hist.append(history[i]-history[i-1])
        if all_zeroes and new_hist[i-1] != 0:
            all_zeroes = False

    if all_zeroes:
        return history[-1]
    else:
        return history[-1] + extrapolate_value_from_history_end(new_hist)

def solve_part1(input_lines):
    extrapolated_values_begin = 0
    for line in input_lines:
        extrapolated_values_begin += extrapolate_value_from_history_end([int(n) for n in line.split(" ")])

    return extrapolated_values_begin

def extrapolate_value_from_history_beginning(history):
    new_hist = []
    all_zeroes = True
    for i in range(1, len(history)):
        new_hist.append(history[i]-history[i-1])
        if all_zeroes and new_hist[i-1] != 0:
            all_zeroes = False

    if all_zeroes:
        return history[0]
    else:
        return history[0] - extrapolate_value_from_history_beginning(new_hist)

def solve_part2(input_lines):
    extrapolated_values_end = 0
    for line in input_lines:
        extrapolated_values_end += extrapolate_value_from_history_beginning([int(n) for n in line.split(" ")])

    return extrapolated_values_end


if __name__ == "__main__":
    input = open(r"day9.txt")
    print("Day 9 Part 1:", solve_part1(input.readlines()))
    input.close()

    input = open(r"day9.txt")
    print("Day 6 Part 2:", solve_part2(input.readlines()))
    input.close()