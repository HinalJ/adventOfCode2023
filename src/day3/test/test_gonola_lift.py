import unittest

from day3.src.gondola_lift import get_missing_part_number


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

if __name__ == '__main__':
    unittest.main()