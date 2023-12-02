import unittest

from day1.src.recoverCalibrationValue import recoverCalibrationValuesPart1, recoverCalibrationValuesPart2


class TestCalibrationValue(unittest.TestCase):
    def test_recoverCalibrationValues1(self):
        testInputLines = open(r"inputTestPart1.txt")
        self.assertEqual(recoverCalibrationValuesPart1(testInputLines.readlines()), 142, "Should be 142")
        testInputLines.close()

        self.assertEqual(recoverCalibrationValuesPart1(["fafzc1jaaskd4ajbfsa5"]), 15, "Should be 15")
        self.assertEqual(recoverCalibrationValuesPart1(["7"]), 77, "Should be 77")


    def test_recoverCalibrationValues2(self):
        testInputLines2 = open(r"inputTestPart2.txt")
        self.assertEqual(recoverCalibrationValuesPart2(testInputLines2.readlines()), 281, "Should be 281")
        testInputLines2.close()

        self.assertEqual(recoverCalibrationValuesPart2(["1nine8nine"]), 19, "Should be 19")
        self.assertEqual(recoverCalibrationValuesPart2(["twone"]), 21, "Should be 21")
        self.assertEqual(recoverCalibrationValuesPart2(["four"]), 44, "Should be 44")

if __name__ == '__main__':
    unittest.main()



