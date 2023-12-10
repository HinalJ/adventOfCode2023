def is_valid_move(direction, pipe_src, pipe_dest):
    valid_moves = [[0, "|", "|"],
                   [0, "|", "7"],
                   [0, "|", "F"],
                   [0, "L", "|"],
                   [0, "L", "7"],
                   [0, "L", "F"],
                   [0, "J", "|"],
                   [0, "J", "7"],
                   [0, "J", "F"],

                   [1, "-", "-"],
                   [1, "-", "7"],
                   [1, "-", "J"],
                   [1, "L", "-"],
                   [1, "L", "7"],
                   [1, "L", "J"],
                   [1, "F", "-"],
                   [1, "F", "7"],
                   [1, "F", "J"],

                   [2, "|", "|"],
                   [2, "|", "J"],
                   [2, "|", "L"],
                   [2, "7", "|"],
                   [2, "7", "J"],
                   [2, "7", "L"],
                   [2, "F", "|"],
                   [2, "F", "J"],
                   [2, "F", "L"],

                   [3, "-", "-"],
                   [3, "-", "F"],
                   [3, "-", "L"],
                   [3, "7", "-"],
                   [3, "7", "F"],
                   [3, "7", "L"],
                   [3, "J", "-"],
                   [3, "J", "F"],
                   [3, "J", "L"],
                   ]

    return valid_moves.__contains__([direction, pipe_src, pipe_dest])
    

def parse_input(input_lines):
    parsed_input = []
    start_idx = (-1, -1)

    for x, line in enumerate(input_lines):
        if start_idx[0] == -1 and line.find("S") != -1:
            start_idx = (x, line.find("S"))
        parsed_input.append(list(line.rstrip()))

    return parsed_input, start_idx


def is_valid_coordinate(coordinate_under_question, allowed_indices):
    if coordinate_under_question[0] < allowed_indices[0] and coordinate_under_question[1]<allowed_indices[1]:
        return True
    else:
        return False
    
    
def get_direction_coordinates(src_idx):
    up = src_idx[0]-1, src_idx[1]
    down = src_idx[0]+1, src_idx[1]
    left = src_idx[0], src_idx[1]-1
    right = src_idx[0], src_idx[1]+1

    return up, right, down, left


def get_valid_moves(pipe_input, src_idx):
    up, right, down, left = get_direction_coordinates(src_idx)
    possible_moves = [up, right, down, left]
    valid_moves = []
    
    for direction, move in enumerate(possible_moves):
        if is_valid_coordinate(move, (len(pipe_input), len(pipe_input[0]))):
            if is_valid_move(direction, pipe_input[src_idx[0]][src_idx[1]], pipe_input[move[0]][move[1]]):
                valid_moves.append(move)

    return valid_moves


def determine_starting_pipe(pipe_input, starting_idx):
    possible_pipes = ["|", "-", "7", "J", "F", "L"]

    for pipe in possible_pipes:
        pipe_input[starting_idx[0]][starting_idx[1]] = pipe

        if len(get_valid_moves(pipe_input, starting_idx)) == 2:
            return pipe_input

    return []


def solve_part1(input_lines):
    parsed_input, starting_idx = parse_input(input_lines)
    determine_starting_pipe(parsed_input, starting_idx)
    possible_moves = get_valid_moves(parsed_input, starting_idx)

    curr_idx = possible_moves[0]
    prev_idx = starting_idx
    counter = 0
    while curr_idx != starting_idx:
        counter += 1
        possible_moves = get_valid_moves(parsed_input, curr_idx)
        tmp = curr_idx
        curr_idx = possible_moves[0] if possible_moves[1] == prev_idx else possible_moves[1]
        prev_idx = tmp

    return counter//2 if counter % 2 == 0 else counter//2 + 1


if __name__ == "__main__":
    print("Day 10:")
    input = open(r"day10.txt")
    print("Part 1: ", solve_part1(input.readlines()))
    input.close()