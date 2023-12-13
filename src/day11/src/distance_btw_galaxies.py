def distance_btw_galaxies(galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols, galaxy_expand=1):
    rows_where_galaxy_not_present = set(range(0, total_rows)) - set(rows_where_galaxy_is_present)
    cols_where_galaxy_not_present = set(range(0, total_cols)) - set(cols_where_galaxy_is_present)

    sum_of_distances = 0

    for i in range(0, len(galaxy_locs)):
        for j in range(i+1, len(galaxy_locs)):
            sum_of_distances += abs(galaxy_locs[j][1] - galaxy_locs[i][1]) + abs(galaxy_locs[j][0] - galaxy_locs[i][0])

            for row in rows_where_galaxy_not_present:
                if galaxy_locs[j][0] < row < galaxy_locs[i][0] or galaxy_locs[j][0] > row > galaxy_locs[i][0]:
                    sum_of_distances += galaxy_expand

            for col in cols_where_galaxy_not_present:
                if galaxy_locs[j][1] < col < galaxy_locs[i][1] or galaxy_locs[j][1] > col > galaxy_locs[i][1]:
                    sum_of_distances += galaxy_expand

    return sum_of_distances


def parse_input(input_lines):
    galaxy_locs = []
    rows_where_galaxy_is_present = []
    cols_where_galaxy_is_present = []
    total_rows = len(input_lines)
    total_cols = 0

    for i, line in enumerate(input_lines):
        if total_cols == 0:
            total_cols = len(line)
        for j, s in enumerate(line):
            if s == "#":
                galaxy_locs.append((i, j))
                rows_where_galaxy_is_present.append(i)
                cols_where_galaxy_is_present.append(j)

    return galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols


def solve_part1(input_lines):
    galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols = parse_input(input_lines)

    return distance_btw_galaxies(galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols)


def solve_part2(input_lines):
    galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols = parse_input(input_lines)

    return distance_btw_galaxies(galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols, galaxy_expand=1000000-1)

if __name__ == "__main__":
    print("Day 11:")

    input = open(r"day11.txt")
    print("Part 1: ", solve_part1(input.readlines()))
    input.close()


    input = open(r"day11.txt")
    print("Part 2: ", solve_part2(input.readlines()))
    input.close()