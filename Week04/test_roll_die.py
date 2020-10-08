"""
Demonstrate how unit test a function that uses random.
Also demonstrates how to mock an object.
"""

from unittest import TestCase
from unittest.mock import patch

import roll_die


class TestRollDie(TestCase):

    def test_roll_one_sided_die_once(self):
        expected = 1
        actual = roll_die.roll_die(1, 1)
        self.assertEqual(expected, actual)

    def test_roll_six_sided_die_once(self):
        actual = roll_die.roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6)

    def test_roll_six_sided_die_twice(self):
        actual = roll_die.roll_die(2, 6)
        self.assertGreaterEqual(actual, 2)
        self.assertLessEqual(actual, 12)

    def test_roll_ten_sided_die_ten_times(self):
        actual = roll_die.roll_die(10, 10)
        self.assertGreaterEqual(actual, 10)
        self.assertLessEqual(actual, 100)

    @patch('random.randint', side_effect=[5])
    def test_roll_die_single_roll(self, mock_randint):
        actual = roll_die.roll_die(3, 3)
        self.assertEqual(actual, 5)

