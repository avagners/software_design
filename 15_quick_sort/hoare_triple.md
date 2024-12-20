### Тройка Хоара для `quickSort`:

`{true}quickSort(arr){arr отсортирован}`

**Предусловие**: `true`, так как алгоритм работает для любого массива.  
**Постусловие**: массив `arr` отсортирован по возрастанию.  

### Тройка Хоара для `partition`:

`{low, high — индексы в arr, pivot = arr[high]}partition(arr, low, high){arr[low ... pivot_index - 1] <= pivot <= arr[pivot_index + 1 ... high]}`

**Предусловие**: `low` и `high` — допустимые индексы массива `arr`.  
**Постусловие**: элементы в `arr` разделены относительно `pivot`, возвращается `pivot_index`.  

## Доказательство корректности  

**Инициализация**: Если подмассив пустой или состоит из одного элемента (базовый случай, когда `low >= high`), он уже отсортирован.

**Сохранение инварианта**: В `partition` массив разделяется на элементы, меньшие и большие `pivot`, так что `pivot` находится на правильной позиции.

**Рекурсивные вызовы**: `quickSort` вызывается для подмассивов `arr[low ... pivot_index - 1]` и `arr[pivot_index + 1 ... high]`, и каждый подмассив сортируется аналогичным образом.

**Завершение**: Когда рекурсия завершается, каждый элемент оказывается на своей позиции, и весь массив `arr` отсортирован.

Таким образом, `quickSort` корректен, так как каждый рекурсивный вызов сортирует подмассивы, а в конечном итоге весь массив становится отсортированным.