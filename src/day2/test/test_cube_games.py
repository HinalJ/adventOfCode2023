import unittest

from day2.src.cube_games import get_valid_games_id, get_power_of_each_game


class Test_Cube_Games(unittest.TestCase):
    def test_get_valid_games_id(self):
        test_input = open("day2Part1TestInput.txt")
        valid_game_ids = get_valid_games_id(test_input.readlines(), [12, 13, 14])
        self.assertEqual(sum(valid_game_ids), 8, "Should be 8")
        test_input.close()

    def test_get_power_of_each_game(self):
        test_input = open("day2Part2TestInput.txt")
        power_of_each_game = get_power_of_each_game(test_input.readlines())
        self.assertEqual(sum(power_of_each_game), 2286, "Should be 2286")
        test_input.close()

if __name__ == '__main__':
    unittest.main()