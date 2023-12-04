import unittest

from day4.src.get_scratched_cards import solve_part1, solve_part2


class Test_Cube_Games(unittest.TestCase):
    def test_get_lottery_card_points(self):
        test_input = open("day4Part1.txt")
        power_of_points = solve_part1(test_input.readlines())
        self.assertEqual(power_of_points, 13, "Should be 13")
        test_input.close()

    def test_get_instances_of_cards(self):
        test_input = open("day4Part1.txt")
        power_of_points = solve_part2(test_input.readlines())
        self.assertEqual(power_of_points, 30, "Should be 30")
        test_input.close()


if __name__ == '__main__':
    unittest.main()
