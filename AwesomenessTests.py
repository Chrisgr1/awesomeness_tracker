import unittest
from unittest.mock import patch
from io import StringIO
from awesomeness_tracker import *

class TestAwesomenessCheck(unittest.TestCase):

    def setUp(self):
        self.awesomeness = AwesomenessCheck("Al", 8000)

    def test_set_awesomeness_level(self):
        self.awesomeness.set_awesomeness_level(8500)
        self.assertEqual(self.awesomeness.awesomeness_level, 8500)


    def test_set_awesomeness_level_type_error(self):
        with self.assertRaises(TypeError):
            self.awesomeness.set_awesomeness_level("not_an_int")

    def test_get_awesomeness_level(self):
        test_cases = [
            (8000, "Awesomeness level is within acceptable limits. As you were, netizen.\nAwesomeness check completed."),
            (9500, "Exception: The user's awesomeness has overloaded the system.\nAwesomeness check completed.")
        ]
        for level, expected_output in test_cases:
            with self.subTest(level=level):
                self.awesomeness.set_awesomeness_level(level)
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    self.awesomeness.get_awesomeness_level()
                    self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_develop_awesomeness_level(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.awesomeness.develop_awesomeness_level()
            self.assertEqual(self.awesomeness.awesomeness_level, 9000)
            self.assertEqual(fake_out.getvalue().strip(), "The data indicate you just became significantly more awesome.")

if __name__ == '__main__':
    unittest.main()
