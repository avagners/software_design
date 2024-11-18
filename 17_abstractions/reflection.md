# Польза абстракций

## Паттерн: Компонент

### Концепция:
**Базовый компонент (Component)**  
Абстрактный класс, определяющий базовые методы, которые должны реализовывать конкретные компоненты.

**Конкретный компонент (Concrete Component)**  
Наследники базового компонента, реализующие специфичное поведение.

**Менеджер компонентов (Component Manager)**  
Управляет всеми зарегистрированными компонентами, обеспечивает их взаимодействие и выполнение задач.

### Пример реализации:
```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List


# Абстрактный компонент
class Component(ABC):
    @abstractmethod
    def initialize(self) -> None:
        """Инициализация компонента."""
        pass

    @abstractmethod
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Выполнение основной логики компонента."""
        pass


# Конкретный компонент для обработки текста
class TextProcessor(Component):
    def initialize(self) -> None:
        print("TextProcessor initialized.")

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        text = data.get("text", "").lower()
        return {"processed_text": text}


# Конкретный компонент для подсчета частоты слов
class WordCounter(Component):
    def initialize(self) -> None:
        print("WordCounter initialized.")

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        text = data.get("processed_text", "")
        word_count = len(text.split())
        return {"word_count": word_count}


# Менеджер компонентов
class ComponentManager:
    def __init__(self):
        self.components: List[Component] = []

    def register_component(self, component: Component) -> None:
        self.components.append(component)
        component.initialize()

    def run_pipeline(self, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        data = initial_data
        for component in self.components:
            data.update(component.execute(data))
        return data


# Использование
if __name__ == "__main__":
    manager = ComponentManager()

    # Регистрируем компоненты
    manager.register_component(TextProcessor())
    manager.register_component(WordCounter())

    # Запуск обработки
    input_data = {"text": "Hello World! This is a test."}
    result = manager.run_pipeline(input_data)
    print(result)
```