from unittest import TestCase
from lab_7 import sparse_add


class TestSparseAdd(TestCase):
    def test_sparse_add_same_single(self):
        """Check out the approach here.
        1. assemble something
        2. assemble something
        3. what do we expect?
        4. execute
        5. assert.
        """
        vector_one = {1: 1}
        vector_two = {1: 1}
        expected = {1: 2}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_different_single(self):

        vector_one = {1: 1}
        vector_two = {2: 1}
        expected = {1: 1, 2: 1}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_overlap(self):
        vector_one = {1: 1, 3: 2, 5: 1}
        vector_two = {3: 2, 4: 2, 5: 2}
        expected = {1: 1, 3: 4, 4: 2, 5: 3}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)
