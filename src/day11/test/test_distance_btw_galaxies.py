import unittest

from day11.src.distance_btw_galaxies import solve_part1, solve_part2, parse_input, distance_btw_galaxies


class Test_Pipe_Maze(unittest.TestCase):
    def test_distance_btw_galaxies_double(self):
        input_lines = open(r"day11Test.txt")
        distance = solve_part1(input_lines.readlines())
        input_lines.close()
        self.assertEqual(distance, 374, "Should be 374")


    def test_distance_btw_galaxies_ten(self):
        input_lines = open(r"day11Test.txt")
        galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols = parse_input(input_lines.readlines())
        distance = distance_btw_galaxies(galaxy_locs, rows_where_galaxy_is_present, cols_where_galaxy_is_present, total_rows, total_cols, galaxy_expand=10-1)
        input_lines.close()
        self.assertEqual(distance, 1030, "Should be 1030")


    def test_distance_btw_galaxies_million(self):
        input_lines = open(r"day11Test.txt")
        distance = solve_part2(input_lines.readlines())
        input_lines.close()
        self.assertEqual(distance, 82000210, "Should be 82000210")



if __name__ == '__main__':
    unittest.main()
