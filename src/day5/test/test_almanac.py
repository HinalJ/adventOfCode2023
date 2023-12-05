import unittest

from day5.src.almanac import solve_part1, solve_part2


class Test_Almanac(unittest.TestCase):
    def test_almanac_part1(self):
        test_input = open("day5Part1.txt")
        nearest_location = solve_part1(test_input.readlines())
        self.assertEqual(nearest_location, 35, "Should be 35")
        test_input.close()

    def test_almanac_part2(self):
        test_input = open("day5Part1.txt")
        nearest_location = solve_part2(test_input.readlines())
        self.assertEqual(nearest_location, 46, "Should be 46")
        test_input.close()


if __name__ == '__main__':
    unittest.main()
