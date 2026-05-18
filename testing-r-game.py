import unittest
from unittest.mock import patch
import randomgame



class TestMain(unittest.TestCase):

    def test_validating_correct_guess(self):
        result = randomgame.validating(3, 3)
        self.assertEqual(result, "You are a genius, the number was: 3")
    
    def test_validating_INcorrect_guess(self):
        result = randomgame.validating(8, 1)
        self.assertEqual(result, "please try again")

    @patch('builtins.input', return_value='6')
    def test_get_usr_input_correctly(self, mock_input):
        result = randomgame.get_user_numb_inp()
        self.assertEqual(result, 6)



if __name__ == "__main__":
    unittest.main()