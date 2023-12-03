import re

def is_symbol(s):
    return s != "." and not s.isdigit() and not s == '\n'

def find_valid_part_number(engine_schematic, symbol_row, symbol_column):
    valid_part_num = {}
    for row_num in [symbol_row-1, symbol_row, symbol_row+1]:
        if len(engine_schematic) > row_num >= 0:
            reading_row = engine_schematic[row_num]
            part_nums = re.findall(r'\d+', reading_row)
            for part_num in part_nums:
                for match in re.finditer(part_num, reading_row):
                    if not reading_row[match.end()].isdigit() and not reading_row[match.start()-1].isdigit() and (match.end()-1 == symbol_column-1 or match.end()-1 == symbol_column or match.end()-1 == symbol_column+1):
                        valid_part_num.update({(row_num, match.start()): int(part_num)})
                    elif not reading_row[match.end()].isdigit() and not reading_row[match.start()-1].isdigit() and (match.start() == symbol_column-1 or match.start() == symbol_column or match.start() == symbol_column+1):
                        valid_part_num.update({(row_num, match.start()): int(part_num)})

    return valid_part_num


def get_missing_part_number(engine_schematic):
    valid_part_num = {}
    symbols = []
    for r, line in enumerate(engine_schematic):
        for c, l in enumerate(list(line)):
            if is_symbol(l):
                symbols.append(l)
                valid_part_num.update(find_valid_part_number(engine_schematic, r, c))

    return valid_part_num.values()


if __name__ == "__main__":
    input = open(r"day3.txt")
    missing_part_number = get_missing_part_number(input.readlines())
    input.close()

    print("Day 3:")
    print("\tPart 1: ", sum(missing_part_number))