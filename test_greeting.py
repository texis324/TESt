import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_default_greeting(self) -> None:
        self.assertEqual(greet(), "ハロー！")

    def test_named_greeting(self) -> None:
        self.assertEqual(greet("世界"), "ハロー、世界さん！")


if __name__ == "__main__":
    unittest.main()
