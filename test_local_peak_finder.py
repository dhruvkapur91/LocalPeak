import unittest


def local_peak(numbers):
    return numbers[0]


class TestLocalPeakFinder(unittest.TestCase):
    def test_local_peak_of_single_element_is_itself(self):
        self.assertEqual(0, local_peak([0]))
        self.assertEqual(1, local_peak([1]))
