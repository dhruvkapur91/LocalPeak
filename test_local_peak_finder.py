import unittest


def local_peak(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if numbers[0] >= numbers[1]:
        return numbers[0]
    else:
        return local_peak(numbers[1:])


class TestLocalPeakFinder(unittest.TestCase):
    def test_local_peak_of_single_element_is_itself(self):
        self.assertEqual(0, local_peak([0]))
        self.assertEqual(1, local_peak([1]))

    def test_local_peak_of_two_same_elements_is_any_of_them(self):
        self.assertEqual(0, local_peak([0, 0]))
        self.assertEqual(1, local_peak([1, 1]))

    def test_local_peak_of_two_elements_is_the_greater_one_of_the_two(self):
        self.assertEqual(1, local_peak([1, 0]))
        self.assertEqual(1, local_peak([0, 1]))

    def test_local_peak_of_three_elements_is_the_greatest_one_of_the_three(self):
        self.assertEqual(2, local_peak([0, 1, 2]))
        self.assertEqual(2, local_peak([2, 1, 0]))
        self.assertEqual(2, local_peak([1, 2, 0]))

    def test_peak_finder_finds_the_first_peak(self):
        data_with_2_peaks = [1, 0, 2]
        self.assertEqual(1, local_peak(data_with_2_peaks))
