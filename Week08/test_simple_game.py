import io
from unittest import TestCase
from unittest.mock import patch

from Week08.acquiring_input import simple_game


class TestSimpleGame(TestCase):

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game(self, mock_output, random_number_generator, mock_input):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You're right!\n"
        self.assertEqual(expected_output, the_game_printed_this)


