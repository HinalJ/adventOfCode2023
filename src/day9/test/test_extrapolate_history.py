import unittest

from day9.src.extrapolate_history import solve_part1_and_part2


class Test_Extrapolate_History(unittest.TestCase):
    def test_extrapolate_value_from_history_beginning(self):
        input_lines = open(r"day9Test.txt")
        extrapolated_values_begin = solve_part1_and_part2(input_lines)[0]
        self.assertEqual(extrapolated_values_begin, 114, "Should be 114")

    def test_extrapolate_value_from_history_end(self):
        input_lines = open(r"day9Test.txt")
        extrapolated_values_end = solve_part1_and_part2(input_lines)[1]
        self.assertEqual(extrapolated_values_end, 2, "Should be 2")



if __name__ == '__main__':
    unittest.main()
