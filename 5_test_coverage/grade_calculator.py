from typing import List


class GradeCalculator:
    def calculate_average(self, grades: List[float]) -> float:
        if not grades:
            raise ValueError("List of grades is empty")
        if any(grade < 1 or grade > 5 for grade in grades):
            raise ValueError("Grades should be between 1 and 5")
        return sum(grades) / len(grades)
