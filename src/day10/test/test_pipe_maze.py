import unittest

from day10.src.pipe_maze import solve_part1


class Test_Pipe_Maze(unittest.TestCase):
    def test_pipe_maze(self):
        input_lines = open(r"day10Test.txt")
        farthest_point = solve_part1(input_lines)
        input_lines.close()
        self.assertEqual(farthest_point, 4, "Should be 4")



if __name__ == '__main__':
    unittest.main()
