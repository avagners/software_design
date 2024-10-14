import unittest
from average_calculator import AverageCalculator


class TestAverageCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = AverageCalculator()

    def test_average_of_positive_numbers(self) -> None:
        numbers = [10, 20, 30, 40]
        result = self.calculator.calculate_average(numbers)
        self.assertEqual(result, 25)

    def test_average_of_negative_numbers(self) -> None:
        numbers = [-10, -20, -30, -40]
        result = self.calculator.calculate_average(numbers)
        self.assertEqual(result, -25)

    def test_average_of_mixed_numbers(self) -> None:
        numbers = [-10, 20, -30, 40]
        result = self.calculator.calculate_average(numbers)
        self.assertEqual(result, 5)

    def test_average_with_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.calculate_average([])

    def test_average_of_single_element(self) -> None:
        numbers = [42]
        result = self.calculator.calculate_average(numbers)
        self.assertEqual(result, 42)

    def test_average_with_none_value(self) -> None:
        numbers = [10, None, 20]
        with self.assertRaises(TypeError):
            self.calculator.calculate_average(numbers)


if __name__ == "__main__":
    unittest.main()
