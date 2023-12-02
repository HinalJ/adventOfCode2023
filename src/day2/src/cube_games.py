from functools import reduce


def get_valid_games_id(games, total_colored_cubes_present):
    color_to_int = {
        "red": 0,
        "green": 1,
        "blue": 2
    }
    valid_game_id = []
    for game in games:
        game_id, sets = game.split(":")
        game_id_int = int(game_id.split(" ")[1])

        invalid_game = False
        for set in sets.split(";"):
            for diff_cubes in set.split(","):
                cubes_no, color = diff_cubes.strip().split(" ")
                if int(cubes_no) > total_colored_cubes_present[color_to_int.get(color)]:
                    invalid_game = True
                    break
            if invalid_game:
                break

        if not invalid_game:
            valid_game_id.append(game_id_int)

    return valid_game_id


# Power is calculated by multiplying minimum number of red, green and blue cubes to be present to make each game valid
def get_power_of_each_game(games):
    color_to_int = {
        "red": 0,
        "green": 1,
        "blue": 2
    }

    power_of_games = []
    for game in games:
        game_id, sets = game.split(":")
        game_id_int = int(game_id.split(" ")[1])

        min_num_of_cubes_req = [0, 0, 0]

        for set in sets.split(";"):
            for diff_cubes in set.split(","):
                cubes_no, color = diff_cubes.strip().split(" ")
                if int(cubes_no) > min_num_of_cubes_req[color_to_int.get(color)]:
                    min_num_of_cubes_req[color_to_int.get(color)] = int(cubes_no)

        power_of_games.append(reduce((lambda x, y: x * y), min_num_of_cubes_req))
    return power_of_games


if __name__ == "__main__":
    input = open(r"day2.txt")
    total_colored_cubes_part1 = [12, 13, 14]  # r g b
    possible_game_ids = get_valid_games_id(input.readlines(), total_colored_cubes_part1)
    input.close()

    input = open(r"day2.txt")
    power_of_each_game = get_power_of_each_game(input.readlines())
    input.close()

    print("Day 2:")
    print("\tPart 1: ", sum(possible_game_ids))
    print("\tPart 2: ", sum(power_of_each_game))
