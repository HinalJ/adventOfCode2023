import unittest

from day6.src.boat_race import num_of_way_win, solve_part2, solve_part1


class Test_Cube_Games(unittest.TestCase):
    def test_get_num_of_ways_to_win_each_race(self):
        product_of_wins = num_of_way_win([7, 15, 30], [9, 40, 200])
        self.assertEqual(product_of_wins, 288, "Should be 288")

    def test_solve_part1(self):
        test_input = open("day6Part1.txt")
        product_of_wins = solve_part1(test_input.readlines())
        self.assertEqual(product_of_wins, 288, "Should be 288")
        test_input.close()

    def test_solve_part2(self):
        test_input = open("day6Part1.txt")
        total_ways_to_win = solve_part2(test_input.readlines())
        self.assertEqual(total_ways_to_win, 71503, "Should be 71503")
        test_input.close()


if __name__ == '__main__':
    unittest.main()
