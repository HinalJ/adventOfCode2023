import unittest

from day3.src.gondola_lift import get_missing_part_number, get_gear_ratio


class Test_Cube_Games(unittest.TestCase):
    def test_get_missing_part_number(self):
        test_input = open("day3Part1TestInput.txt")
        missing_part_number = get_missing_part_number(test_input.readlines())
        self.assertEqual(sum(missing_part_number), 4361, "Should be 4361")
        test_input.close()

    def test_get_missing_part_number2(self):
        test_input2 = open("part1Test2.txt")
        missing_part_number = get_missing_part_number(test_input2.readlines())
        self.assertEqual(sum(missing_part_number), 237, "Should be 237")
        test_input2.close()

    def test_get_gear_ratio(self):
        test_input = open("day3Part1TestInput.txt")
        sum_of_gear_ratios = get_gear_ratio(test_input.readlines(), 2)
        self.assertEqual(sum_of_gear_ratios, 467835, "Should be 467835")
        test_input.close()

    def test_get_gear_ratio2(self):
        test_input2 = open("part2Test2.txt")
        sum_of_gear_ratios = get_gear_ratio(test_input2.readlines(), 2)
        self.assertEqual(sum_of_gear_ratios, 343742, "Should be 343742")
        test_input2.close()

if __name__ == '__main__':
    unittest.main()