import unittest
import modulesinPython

class TestMain(unittest.TestCase):

    def setUp(self):
        print("About to test a function")

    def test_do_stuff(self):
        test_param = 10
        result = modulesinPython.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "akdjkfjd"
        result = modulesinPython.do_stuff(test_param)
        self.assertEqual(result, "please enter number")


    def test_do_stuff3(self):
        test_param = None
        result = modulesinPython.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)


    def test_do_stuff4(self):
        test_param = ""
        result = modulesinPython.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff5(self):
        test_param = 0
        result = modulesinPython.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('cleaning up')

if __name__ == "__main__":
    unittest.main()
