from typing import List


def quickSort(arr: List[int]) -> None:
    def _quickSort(arr: List[int], low: int, high: int) -> None:
        if low < high:
            pivot_index = partition(arr, low, high)
            _quickSort(arr, low, pivot_index - 1)
            _quickSort(arr, pivot_index + 1, high)

    def partition(arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Запускаем внутреннюю рекурсивную сортировку на всем массиве
    _quickSort(arr, 0, len(arr) - 1)
