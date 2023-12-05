def init(source_nums):
    d = {}
    for n in source_nums:
        d.update({n: n})
    return d


def calculate_destination_value(source_nums, dest_to_source_maps):
    source_to_dest_map_init = init(source_nums)

    for source_num in source_nums:
        for each_map in dest_to_source_maps:
            if each_map[1] + each_map[2] > source_num >= each_map[1]:
                source_to_dest_map_init.update(
                    {source_num: (source_num - each_map[1]) + each_map[0]})

    return source_to_dest_map_init.values()


def solve_part1(input_lines):
    all_maps_names = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    all_maps_list = [[] for _ in all_maps_names]

    counter = 0
    curr_source_num = []
    curr_src_to_nxt_dest_map = []
    for idx, line in enumerate(input_lines):
        if line.startswith("seeds"):
            curr_source_num = [int(n) for n in line.split(":")[1].strip().split(" ")]
            all_maps_list[counter] = [int(n) for n in curr_source_num]
        elif line == '\n' or len(input_lines) == idx:
            counter += 1
            all_maps_list[counter] = calculate_destination_value(curr_source_num, curr_src_to_nxt_dest_map)
        elif ":" in line:
            curr_source_num = all_maps_list[counter]
            curr_src_to_nxt_dest_map = []
        else:
            curr_src_to_nxt_dest_map.append([int(n) for n in line.split(" ")])

    return min(all_maps_list[-1])

def parse_to_range(seeds_list):
    seed_range = {}
    x = -1

    for idx, seeds in enumerate(seeds_list):
        if idx % 2 == 0:
            x = seeds_list[idx]
        else:
            seed_range.update({(x, x + seeds_list[idx]): 0})

    return seed_range

def update_the_range(source_range, dest_range_maps):
    updated_source_range = {}
    dd, ds, step = dest_range_maps

    for x, y in source_range.keys():
        if x >= ds + step or y <= ds:
            updated_source_range.update({(x, y): source_range.get((x, y), 0)})
        elif ds <= x and ds+step >= y:
            updated_source_range.update({(x, y): dd-ds})
        else:
            if x < ds <= y <= ds+step:
                updated_source_range.update({(x, ds): source_range.get((x, y), 0)})
                updated_source_range.update({(ds, y): dd-ds})
            elif ds <= x < ds+step <= y:
                updated_source_range.update({(x, ds+step): dd-ds})
                updated_source_range.update({(ds+step, y): source_range.get((x, y), 0)})
            else:  # x < ds < ds+step < y
                updated_source_range.update({(x, ds): source_range.get((x, y), 0)})
                updated_source_range.update({(ds, ds+step): dd-ds})
                updated_source_range.update({(ds+step, y): source_range.get((x, y), 0)})

    return updated_source_range

def map_to_new_dim(curr_dictionary):
    updated_dictionary = {}
    for (x, y), v in curr_dictionary.items():
        updated_dictionary.update({(x+v, y+v): 0})

    return updated_dictionary

def solve_part2(input_lines):
    all_maps_names = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    all_maps_list = [{} for _ in all_maps_names]

    counter = 0
    curr_src_to_nxt_dest_map = []

    for idx, line in enumerate(input_lines):
        if line.startswith("seeds"):
            curr_source_num = [int(n) for n in line.split(":")[1].strip().split(" ")]
            all_maps_list[counter] = parse_to_range([int(n) for n in curr_source_num])
        elif line == '\n' or len(input_lines) == idx:
            counter += 1
            for i, each_map in enumerate(curr_src_to_nxt_dest_map):
                if i == 0:
                    all_maps_list[counter] = update_the_range(all_maps_list[counter-1], each_map)
                else:
                    all_maps_list[counter] = update_the_range(all_maps_list[counter], each_map)
            all_maps_list[counter] = map_to_new_dim(all_maps_list[counter])

        elif ":" in line:
            curr_src_to_nxt_dest_map = []
        else:
            curr_src_to_nxt_dest_map.append([int(n) for n in line.split(" ")])

    return min([x for x, y in all_maps_list[-1].keys()])


if __name__ == "__main__":
    input = open(r"day5.txt")
    print("Day 5 Part 1:", solve_part1(input.readlines()))
    input.close()

    input = open(r"day5.txt")
    print("Day 5 Part 2:", solve_part2(input.readlines()))
    input.close()
