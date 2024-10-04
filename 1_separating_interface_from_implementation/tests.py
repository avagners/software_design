import os
import json
import unittest

from storage import DBStorage, InMemoryStorage, FileStorage


class TestDBStorage(unittest.TestCase):

    def setUp(self) -> None:
        """
        Этот метод выполняется перед каждым тестом. Он создает новый экземпляр
        базы данных для тестирования и использует временную базу данных.
        """
        self.db_name = "test_storage.db"
        self.storage = DBStorage(db_name=self.db_name)

    def tearDown(self) -> None:
        """
        Этот метод выполняется после каждого теста. Он удаляет временную базу данных.
        """
        self.storage = None
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_save_and_retrieve_existing(self) -> None:
        """Тестируем сохранение и успешное извлечение существующих данных."""
        self.storage.save("Test Data 1")
        self.storage.save("Test Data 2")
        self.storage.save("Test Data 3")

        # Проверяем, что данные успешно извлекаются по ID
        self.assertEqual(self.storage.retrieve(1), "Test Data 1")
        self.assertEqual(self.storage.retrieve(2), "Test Data 2")
        self.assertEqual(self.storage.retrieve(3), "Test Data 3")

    def test_retrieve_non_existing(self) -> None:
        """Тестируем извлечение данных по несуществующему ID."""
        # Сначала сохраняем несколько записей
        self.storage.save("Test Data 1")
        self.storage.save("Test Data 2")

        # Запрашиваем несуществующий ID
        self.assertIsNone(self.storage.retrieve(999))  # ID 999 не должен существовать

    def test_retrieve_empty_table(self) -> None:
        """Тестируем извлечение данных из пустой таблицы."""
        # Таблица пуста, ни одной записи нет
        self.assertIsNone(self.storage.retrieve(1))  # Не должно ничего возвращаться

    def test_sequential_ids(self) -> None:
        """Тестируем, что ID сохраняются последовательно."""
        self.storage.save("First")
        self.storage.save("Second")
        self.storage.save("Third")

        # Проверяем, что каждая запись получила последовательный ID
        self.assertEqual(self.storage.retrieve(1), "First")
        self.assertEqual(self.storage.retrieve(2), "Second")
        self.assertEqual(self.storage.retrieve(3), "Third")

    def test_save_and_retrieve_empty_string(self):
        """Тест на сохранение и извлечение пустой строки."""
        self.storage.save("")
        self.assertEqual(self.storage.retrieve(1), "")


class TestInMemoryStorage(unittest.TestCase):

    def setUp(self):
        """Инициализация перед каждым тестом: создаём новое хранилище в памяти."""
        self.storage = InMemoryStorage()

    def test_save_and_retrieve(self):
        """Тест на корректное сохранение и извлечение данных."""
        self.storage.save("Test Data 1")
        self.storage.save("Test Data 2")

        self.assertEqual(self.storage.retrieve(0), "Test Data 1")
        self.assertEqual(self.storage.retrieve(1), "Test Data 2")

    def test_retrieve_non_existent(self):
        """Тест на извлечение несуществующего ID."""
        self.assertIsNone(self.storage.retrieve(999))

    def test_save_and_retrieve_empty_string(self):
        """Тест на сохранение и извлечение пустой строки."""
        self.storage.save("")
        self.assertEqual(self.storage.retrieve(0), "")


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Инициализация перед каждым тестом: создаём новое хранилище в файле."""
        self.file_name = "test_storage.json"
        self.storage = FileStorage(self.file_name)

    def tearDown(self):
        """Очистка после каждого теста: удаляем тестовый файл."""
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_save_and_retrieve(self):
        """Тест на корректное сохранение и извлечение данных."""
        self.storage.save("Test Data 1")
        self.storage.save("Test Data 2")

        self.assertEqual(self.storage.retrieve(0), "Test Data 1")
        self.assertEqual(self.storage.retrieve(1), "Test Data 2")

    def test_retrieve_non_existent(self):
        """Тест на извлечение несуществующего ID."""
        self.assertIsNone(self.storage.retrieve(999))

    def test_save_and_retrieve_empty_string(self):
        """Тест на сохранение и извлечение пустой строки."""
        self.storage.save("")
        self.assertEqual(self.storage.retrieve(0), "")

    def test_load_from_file(self):
        """Тест на загрузку данных из файла при создании хранилища."""
        # Сохраним данные напрямую в файл для проверки загрузки
        with open(self.file_name, 'w') as file:
            json.dump({0: "Test Data 1", 1: "Test Data 2"}, file)

        # Теперь создаём объект FileStorage и проверяем загрузку
        new_storage = FileStorage(self.file_name)
        self.assertEqual(new_storage.retrieve(0), "Test Data 1")
        self.assertEqual(new_storage.retrieve(1), "Test Data 2")


if __name__ == '__main__':
    unittest.main()
