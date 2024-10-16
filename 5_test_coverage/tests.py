import unittest
from grade_calculator import GradeCalculator


class TestGradeCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = GradeCalculator()

    # 1. Тест на обычные валидные значения (1-5)
    def test_average_of_valid_grades(self) -> None:
        grades = [3, 4, 5, 2, 4]
        result = self.calculator.calculate_average(grades)
        self.assertEqual(result, 3.6)

    # 2. Тест на пустой список
    def test_average_with_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.calculate_average([])

    # 3. Тест на наличие оценки меньше 1 (невалидные данные)
    def test_average_with_grade_below_1(self) -> None:
        grades = [3, 0, 4]
        with self.assertRaises(ValueError):
            self.calculator.calculate_average(grades)

    # 4. Тест на наличие оценки больше 5 (невалидные данные)
    def test_average_with_grade_above_5(self) -> None:
        grades = [3, 6, 4]
        with self.assertRaises(ValueError):
            self.calculator.calculate_average(grades)

    # 5. Тест на крайние граничные значения (1 и 5)
    def test_average_with_boundary_grades(self) -> None:
        grades = [1, 5, 5, 1]
        result = self.calculator.calculate_average(grades)
        self.assertEqual(result, 3.0)


if __name__ == "__main__":
    unittest.main()
