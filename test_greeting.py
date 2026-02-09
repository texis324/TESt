import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_default_greeting(self) -> None:
        self.assertEqual(greet(), "こんにちは！")

    def test_named_greeting(self) -> None:
        self.assertEqual(greet("世界"), "こんにちは、世界さん！")


if __name__ == "__main__":
    unittest.main()
