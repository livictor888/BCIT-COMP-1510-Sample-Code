import io
from unittest import TestCase
from unittest.mock import patch

from Sandbox.Assorted.acquiring_input import simple_game


class TestSimpleGame(TestCase):

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1, 10, 5])
    def test_simple_game(self, mock_input, mock_output, random_number_generator):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You're right!\n"
        self.assertEqual(expected_output, the_game_printed_this)
