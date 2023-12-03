import re


def is_symbol(s):
    return s != "." and not s.isdigit() and not s == '\n'


def find_valid_part_number(engine_schematic, symbol_row, symbol_column):
    valid_part_num = {}
    for row_num in [symbol_row - 1, symbol_row, symbol_row + 1]:
        if len(engine_schematic) > row_num >= 0:
            reading_row = engine_schematic[row_num]
            part_nums = re.findall(r'\d+', reading_row)
            for part_num in set(part_nums):
                for match in re.finditer(part_num, reading_row):
                    # Need to remove the ones that have false search like searching 3 in ..3...234.. should result only
                    # one and not two entries
                    if not reading_row[match.end()].isdigit() and not reading_row[match.start() - 1].isdigit():
                        if match.end() - 1 == symbol_column - 1 or match.end() - 1 == symbol_column or match.end() - 1 == symbol_column + 1:
                            valid_part_num.update({(row_num, match.start()): int(part_num)})
                        elif match.start() == symbol_column - 1 or match.start() == symbol_column or match.start() == symbol_column + 1:
                            valid_part_num.update({(row_num, match.start()): int(part_num)})

    return valid_part_num


def get_missing_part_number(engine_schematic):
    valid_part_num = {}

    for r, line in enumerate(engine_schematic):
        for c, l in enumerate(list(line)):
            if is_symbol(l):
                valid_part_num.update(find_valid_part_number(engine_schematic, r, c))

    return valid_part_num.values()


def find_gear_ratio_of_symbol(engine_schematic, symbol_row, symbol_column, valid_gear, symbol):
    valid_part_num = []

    if not symbol == '*':
        return 0

    for row_num in [symbol_row - 1, symbol_row, symbol_row + 1]:
        if len(engine_schematic) > row_num >= 0:
            reading_row = engine_schematic[row_num]
            part_nums = re.findall(r'\d+', reading_row)
            for part_num in set(part_nums):
                for match in re.finditer(part_num, reading_row):
                    # Need to remove the ones that have false search like searching 3 in ..3...234.. should result only
                    # one and not two entries
                    if not reading_row[match.end()].isdigit() and not reading_row[match.start() - 1].isdigit():
                        if match.end() - 1 == symbol_column - 1 or match.end() - 1 == symbol_column or match.end() - 1 == symbol_column + 1:
                            valid_part_num.append(int(part_num))
                        elif match.start() == symbol_column - 1 or match.start() == symbol_column or match.start() == symbol_column + 1:
                            valid_part_num.append(int(part_num))

    if len(valid_part_num) == valid_gear:
        return valid_part_num[0]*valid_part_num[1]
    else:
        return 0


def get_gear_ratio(engine_schematic, valid_gear):
    sum_of_gear_ratios = 0

    for r, line in enumerate(engine_schematic):
        for c, l in enumerate(list(line)):
            if is_symbol(l):
                sum_of_gear_ratios += find_gear_ratio_of_symbol(engine_schematic, r, c, valid_gear, l)

    return sum_of_gear_ratios

if __name__ == "__main__":
    input = open(r"day3.txt")
    missing_part_number = get_missing_part_number(input.readlines())
    input.close()

    input = open(r"day3.txt")
    valid_gear_value = 2  # Part Number
    sum_of_gear_ratios = get_gear_ratio(input.readlines(), valid_gear_value)
    input.close()

    print("Day 3:")
    print("\tPart 1: ", sum(missing_part_number))
    print("\tPart 2: ", sum_of_gear_ratios)
