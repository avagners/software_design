```python
def max(a, b):
    return a if a >= b else b


def abs(x):
    return x if x >= 0 else -x


def maxAbs(a, b):
    absA = abs(a)
    absB = abs(b)
    return max(absA, absB)
```
## Доказательство корректности maxAbs(a, b)

Функция `maxAbs(a, b)` состоит из трех шагов: вызовов `abs(a)`, `abs(b)`, и `max(absA, absB)`. Докажем корректность каждого из этих шагов с помощью троек Хоара и объединим их.

1. Предусловие: true

2. Тело функции (команды):

Шаг 1: Вычисление `absA = abs(a)`

Команда: absA = abs(a)  
Постусловие: absA=∣a∣  
Тройка Хоара: {true}absA = abs(a){absA=∣a∣}  

Шаг 2: Вычисление `absB = abs(b)`

Команда: absB = abs(b)  
Постусловие: absB=∣b∣  
Тройка Хоара: {true}absB = abs(b){absB=∣b∣}  

Шаг 3: Вычисление `result = max(absA, absB)`

Команда: result = max(absA, absB)  
Постусловие: result = max(∣a∣,∣b∣)  
Тройка Хоара: {absA=∣a∣ ∧ absB=∣b∣} result = max(absA, absB){result=max(∣a∣,∣b∣)}                                                                                                                                                             

3. Постусловие для всей функции: result=max(∣a∣,∣b∣)

### Композиция  
Собрав все шаги в композицию троек Хоара для всей функции `maxAbs`, получаем:

{true}absA = abs(a); absB = abs(b); result = max(absA, absB){result=max(∣a∣,∣b∣)}

Таким образом, доказано, что функция `maxAbs(a, b)` корректно вычисляет максимум модуля двух чисел.