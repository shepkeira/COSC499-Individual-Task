import builtins
import unittest
from unittest import mock
from unittest.mock import patch
from random import randint

from number_picker import accept_guess, guess_number, compare_number

class TestGuesser(unittest.TestCase):
    def test_compare_number_correct(self):
        num = 50
        guess = 50
        msg, success = compare_number(num, guess)
        self.assertEqual(num, guess)
        self.assertEqual(msg, "Correct!")
        self.assertTrue(success)
    def test_change_guess_too_high(self):
        num = 50
        guess = 75
        msg, success = compare_number(num, guess)
        self.assertEqual(msg, "Too high guess again")
        self.assertFalse(success)
    def test_change_guess_too_low(self):
        num = 50
        guess = 25
        msg, success = compare_number(num, guess)
        self.assertEqual(msg, "Too low guess again")
        self.assertFalse(success)
    def test_pick_number_25(self):
        user_input = ["25"]
        with patch('builtins.input', side_effect=user_input):
            response = accept_guess()
        self.assertEqual(response, 25)
    def test_pick_number_a(self):
        user_input = ["a", "25"]
        with patch('builtins.input', side_effect=user_input):
            response = accept_guess()
        self.assertEqual(response, 25)
    @patch('number_picker.input')
    @patch('number_picker.randint')
    def test_guess_number(self, mock_input, mock_randint):
        mock_input.side_effect = ["25"]
        mock_randint.side_effect = [25]
        response = guess_number()
        self.assertEqual(response, 25)


if __name__ == '__main__':
    unittest.main()