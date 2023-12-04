def parsed_cards(input_lines):
    cards_nums = []
    for line in input_lines:
        colon_split = line.split(":")
        lottery_nums_str, my_nums_str = colon_split[1].split("|")
        lottery_nums = [int(ln.strip()) for ln in lottery_nums_str.strip().split(" ") if ln != '']
        my_nums = [int(nm.strip()) for nm in my_nums_str.strip().split(" ") if nm != '']
        cards_nums.append((lottery_nums, my_nums))

    return cards_nums


def get_lottery_card_points(lottery_num, my_card_num):
    matching_nums = [num for num in my_card_num if num in lottery_num]
    return len(matching_nums)


def power_points_cards(matching_nums):
    sum_of_points = 0

    for n in matching_nums:
        if n != 0:
            sum_of_points += pow(2, n - 1)

    return sum_of_points


def solve_part1(input_lines):
    card_matching_nums = []

    for lottery_nums, my_nums in parsed_cards(input_lines):
        card_matching_nums.append(get_lottery_card_points(lottery_nums, my_nums))

    return power_points_cards(card_matching_nums)


def solve_part2(input_lines):
    total_cards = len(input_lines)

    def init_cards(num_of_cards):
        return [1 for _ in range(0, num_of_cards)]

    instance_of_cards = init_cards(total_cards)
    card_matching_nums = []
    for lottery_nums, my_nums in parsed_cards(input_lines):
        card_matching_nums.append(get_lottery_card_points(lottery_nums, my_nums))

    for i in range(0, total_cards):
        copy_cards = card_matching_nums[i]

        for _ in range(0, instance_of_cards[i]):
            for j in range(i + 1, i + copy_cards + 1):
                instance_of_cards[j] += 1

    return sum(instance_of_cards)


if __name__ == "__main__":
    input = open(r"day4.txt")
    print("Day 4 Part 1:", solve_part1(input.readlines()))
    input.close()

    input = open(r"day4.txt")
    print("Day 4 Part 2:", solve_part2(input.readlines()))
    input.close()
