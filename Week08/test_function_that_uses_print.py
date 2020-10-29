"""
Demonstrate how to mock an object.
"""

from unittest import TestCase
import unittest.mock
import io

import Week08.using_a_print_function as using_a_print_function


class TestMyPrinter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_my_printer(self, mock_stdout):
        using_a_print_function.my_printer("Hello world!")
        expected = "Hello world!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)


