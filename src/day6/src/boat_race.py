def num_of_way_win(time_of_races, current_highest_distances):
    num_of_ways_to_win_each_race = 1
    for idx, time_of_race in enumerate(time_of_races):
        win_counter = 0
        for i in range(0, time_of_race+1):
            if i*(time_of_race-i) > current_highest_distances[idx]:
                win_counter += 1
        num_of_ways_to_win_each_race *= win_counter

    return num_of_ways_to_win_each_race

def solve_part1(input_lines):
    race_times = []
    farthest_distances = []
    for line in input_lines:
        if "Time" in line:
            race_times_inp = line.split(":")[1].strip()
            race_times = [int(t) for t in race_times_inp.split(" ") if t != '']
        else:
            farthest_distances_inp = line.split(":")[1].strip()
            farthest_distances = [int(f) for f in farthest_distances_inp.split(" ") if f != '']

    return num_of_way_win(race_times, farthest_distances)

def solve_part2(input_lines):
    race_times = []
    farthest_distances = []
    for line in input_lines:
        if "Time" in line:
            race_times_inp = line.split(":")[1].strip()
            race_times = [int(race_times_inp.replace(" ", ""))]
        else:
            farthest_distances_inp = line.split(":")[1].strip()
            farthest_distances = [int(farthest_distances_inp.replace(" ", ""))]

    return num_of_way_win(race_times, farthest_distances)

if __name__ == "__main__":
    input = open(r"day6.txt")
    print("Day 6 Part 1:", solve_part1(input.readlines()))
    input.close()

    input = open(r"day6.txt")
    print("Day 6 Part 2:", solve_part2(input.readlines()))
    input.close()
