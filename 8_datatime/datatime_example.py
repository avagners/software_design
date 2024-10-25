'''
Недостатки в примере на Java:

1) SimpleDateFormat по умолчанию использует часовой пояс системы.
Если система работает в одном часовом поясе, а дата создается для
другого, это может привести к ошибкам.
2) SimpleDateFormat является неустойчивым к изменениям, если дата
не соответствует формату — это приводит к исключениям.

Ниже улучшенный вариант на Python.
'''
from datetime import datetime
import pytz

# Определяем формат даты
date_string = "2024-05-13 14:30:00"
date_format = "%Y-%m-%d %H:%M:%S"

# Определяем часовой пояс для работы, например, UTC
timezone = pytz.timezone("UTC")

try:
    # Парсим строку в объект datetime
    naive_date = datetime.strptime(date_string, date_format)
    # Присваиваем часовому поясу
    date = timezone.localize(naive_date)
    print("Date:", date)
except ValueError as e:
    print("Error parsing date:", e)
