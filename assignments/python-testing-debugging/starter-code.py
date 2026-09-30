import unittest


def is_even(number):
    return number % 2 == 0


def count_vowels(text):
    return sum(1 for character in text if character in "aeiou")


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


class HelperFunctionTests(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("school"), 2)

    def test_calculate_average(self):
        self.assertEqual(calculate_average([2, 4, 6]), 4)


if __name__ == "__main__":
    unittest.main()