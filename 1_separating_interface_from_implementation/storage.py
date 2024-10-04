import os
import json
import sqlite3

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar, override

T = TypeVar('T')


# АТД Storage
class Storage(ABC, Generic[T]):
    # Конструктор
    # постусловие: создана пустое хранилище
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: новый элемент сохранен в хранилище
    @abstractmethod
    def save(self, data: str) -> None: ...

    # Запросы:
    @abstractmethod
    def retrieve(self, id: int) -> Optional[str]: ...  # элемент из хранилища


# Реализация хранилища, сохраняющая данные в памяти
class InMemoryStorage(Storage):
    def __init__(self) -> None:
        super().__init__()
        self._storage: Dict[int, str] = dict()
        self._counter: int = 0

    @override
    def save(self, data: str) -> None:
        self._storage[self._counter] = data
        self._counter += 1

    @override
    def retrieve(self, id: int) -> Optional[str]:
        return self._storage.get(id)


# Реализация хранилища, сохраняющая данные в файл
class FileStorage(Storage):
    def __init__(self, file_name: str = "storage.json") -> None:
        super().__init__()
        self._file: str = file_name
        self._storage: Dict[int, str] = self._load_from_file()

    @override
    def save(self, data: str) -> None:
        id = len(self._storage)
        self._storage[id] = data
        self._save_to_file()

    @override
    def retrieve(self, id: int) -> Optional[str]:
        return self._storage.get(id)

    def _save_to_file(self) -> None:
        with open(self._file, "w") as file:
            json.dump(self._storage, file)

    def _load_from_file(self) -> Dict[int, str]:
        if not os.path.exists(self._file):
            return {}
        with open(self._file, "r") as file:
            data = json.load(file)
            # Преобразование ключей в int
            return {int(key): value for key, value in data.items()}


# Реализация хранилища, сохраняющая данные в базе данных
class DBStorage(Storage):
    def __init__(self, db_name: str = "storage.db") -> None:
        self.db_name: str = db_name
        self._initialize_database()

    def _initialize_database(self) -> None:
        with sqlite3.connect(self.db_name) as connection:
            connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS storage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL
                )
                '''
            )

    @override
    def save(self, data: str) -> None:
        with sqlite3.connect(self.db_name) as connection:
            connection.execute('INSERT INTO storage (data) VALUES (?)', (data,))

    @override
    def retrieve(self, id: int) -> Optional[str]:
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT data FROM storage WHERE id = ?', (id,))
            row = cursor.fetchone()
        return row[0] if row else None


if __name__ == "__main__":
    storage: DBStorage = DBStorage()

    # Сохраняем данные
    storage.save("Data 1")
    storage.save("Data 2")
    storage.save("Data 3")

    # Извлекаем данные по ID
    print("Data at ID 1:", storage.retrieve(101))
    print("Data at ID 2:", storage.retrieve(2))
    print("Data at ID 3:", storage.retrieve(3))
