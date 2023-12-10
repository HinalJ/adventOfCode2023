def extrapolate_value_from_history(history, isEnd=True):
    new_hist = []
    all_zeroes = True
    for i in range(1, len(history)):
        new_hist.append(history[i]-history[i-1])
        if all_zeroes and new_hist[i-1] != 0:
            all_zeroes = False

    if all_zeroes:
        return history[-1] if isEnd else history[0]
    else:
        return history[-1] + extrapolate_value_from_history(new_hist) if isEnd \
            else history[0] - extrapolate_value_from_history(new_hist, False)


def solve_part1_and_part2(input_lines):
    extrapolated_values_begin = 0
    extrapolated_values_end = 0
    for line in input_lines:
        extrapolated_values_begin += extrapolate_value_from_history([int(n) for n in line.split(" ")])
        extrapolated_values_end += extrapolate_value_from_history([int(n) for n in line.split(" ")], False)

    return extrapolated_values_begin, extrapolated_values_end


if __name__ == "__main__":
    input = open(r"day9.txt")
    part1, part2 = solve_part1_and_part2(input.readlines())
    input.close()

    print("Day 9 Part 1:", part1)
    print("Day 9 Part 2:", part2)
