import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")
        self.assertEqual(awesome.frown(), ":(")
        self.assertEqual(awesome.some_other_func(), ":/")
        self.assertEqual(awesome.yet_other_func(), ":/")


if __name__ == '__main__':
    unittest.main()
