import unittest

from day10.src.pipe_maze import solve_part1, solve_part2


class Test_Pipe_Maze(unittest.TestCase):
    def test_pipe_maze(self):
        input_lines = open(r"day10TestPart1.txt")
        farthest_point = solve_part1(input_lines)
        input_lines.close()
        self.assertEqual(farthest_point, 4, "Should be 4")


    def test_pipe_maze_area(self):
        input_lines = open(r"day10TestPart2.txt")
        farthest_point = solve_part2(input_lines)
        input_lines.close()
        self.assertEqual(farthest_point, 8, "Should be 8")



if __name__ == '__main__':
    unittest.main()
