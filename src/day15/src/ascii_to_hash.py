def solve_part1(input_lines):
    sum_of_init = 0
    num = 0
    for line in input_lines:

        for ch in line:
            if ch != ',':
                num += ord(ch)
                num *= 17
                num %= 256
            else:
                sum_of_init += num
                num = 0

    return sum_of_init + num


def focal_powers(boxes):
    focal_power = 0
    for box_num, label_to_focal in boxes.items():
        for pos, focal_length in enumerate(label_to_focal.values()):
            focal_power += box_num * (pos + 1) * focal_length

    return focal_power


def solve_part2(input_lines):
    num = 0
    boxes = {}

    for line in input_lines:
        label = ''
        for ch in line:
            if ch == '=':
                pass
            elif ch.isdigit():
                tmp_dict = boxes.get(num+1, {})
                tmp_dict.update({label: int(ch)})
                boxes.update({num+1: tmp_dict})
                label = ''
            elif ch == '-':
                tmp_dict = {key: val for key, val in boxes.get(num+1, {}).items() if key != label}
                boxes.update({num+1: tmp_dict})
                label = ''
            elif ch != ',':
                num += ord(ch)
                num *= 17
                num %= 256
                label += ch
            else:
                num = 0

    return focal_powers(boxes)


if __name__ == "__main__":
    print("Day15")
    input = open(r"day15.txt")
    print("Part1:", solve_part1(input.readlines()))

    input = open(r"day15.txt")
    print("Part2:", solve_part2(input.readlines()))
