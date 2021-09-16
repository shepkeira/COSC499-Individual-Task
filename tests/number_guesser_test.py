import builtins
import unittest
from unittest.mock import patch

from number_guesser import change_guess, pick_number

class TestGuesser(unittest.TestCase):
    def test_change_guess_correct(self):
        high = 100
        low = 0
        guess = 50
        ans = 'A'
        new_guess, done = change_guess(ans, guess, high, low)
        self.assertAlmostEqual(new_guess, guess)
        self.assertTrue(done)
    def test_change_guess_incorrect_resonse(self):
        high = 100
        low = 0
        guess = 50
        ans = 'D'
        new_guess, done = change_guess(ans, guess, high, low)
        self.assertAlmostEqual(new_guess, guess)
        self.assertFalse(done)
    def test_change_guess_too_high(self):
        high = 100
        low = 0
        guess = 50
        ans = 'B'
        new_guess, done = change_guess(ans, guess, high, low)
        self.assertAlmostEqual(new_guess, 25)
        self.assertFalse(done)
    def test_change_guess_too_low(self):
        high = 100
        low = 0
        guess = 50
        ans = 'C'
        new_guess, done = change_guess(ans, guess, high, low)
        self.assertAlmostEqual(new_guess, 75)
        self.assertFalse(done)
    def test_pick_number_50(self):
        user_input = ["A"]
        with patch('builtins.input', side_effect=user_input):
            response = pick_number()
        self.assertEqual(response, 50)
    def test_pick_number_25(self):
        user_input = ["B", "A"]
        with patch('builtins.input', side_effect=user_input):
            response = pick_number()
        self.assertEqual(response, 25)
    def test_pick_number_75(self):
        user_input = ["C", "A"]
        with patch('builtins.input', side_effect=user_input):
            response = pick_number()
        self.assertEqual(response, 75)


if __name__ == '__main__':
    unittest.main()