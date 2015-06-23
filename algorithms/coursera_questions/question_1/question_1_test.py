import unittest

from question_1 import count_inversions_brute_force, count_inversions


class CountInversionsTest(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ([1, 3, 5, 2, 4, 6], 3),
            ([1, 5, 3, 2, 4], 4),
            ([5, 4, 3, 2, 1], 10),
            ([1, 6, 3, 2, 4, 5], 5)
        ]

    def test_brute_force(self):
        for test in self.test_cases:
            result = count_inversions_brute_force(test[0])
            self.assertEqual(result, test[1])

    def test_recursive(self):
        for test in self.test_cases:
            result = count_inversions(test[0])
            self.assertEqual(result, test[1])
