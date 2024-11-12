# "Знание" кода

## Задание 1.
```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    // Переопределение метода makeSound
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myCat = new Cat();
        myCat.makeSound();  // "Meow"
    }
}
```

Но если
```java
class Animal {
    // Изменен метод в суперклассе
    public void makeGenericSound() {
        System.out.println("Some generic animal sound");
    }
}
```

### Вопрос:
Как теперь отработает программа?

### Ответ:
Мы получим ошибку `The method makeSound() is undefined for the type Animal`. 

Это связано с тем, что класс `Cat` является наследником от класса `Animal`. Класс `Cat` **зависит** от класса `Animal`. `Cat` "знает" о методах `Animal`. Поэтому после изменения наименования метода `makeSound` на `makeGenericSound` в классе `Animal` мы получаем указанную выше ошибку, так как в классе `Cat` мы пытемя переопределить несуществующий метод класса `Animal`.

### Задание 2.
```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound(int numberOfSounds) {
        for (int i = 0; i < numberOfSounds; i++) {
            System.out.println("Meow");
        }
    }
    
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.makeSound();
        cat.makeSound(3);
    }
}
```

### Вопрос:
Как отработает такая программа?

### Ответ:

Мы получим ошибку `The method makeSound() in the type Animal is not applicable for the arguments (int)`. 

Это также связано с тем, что класс `Cat` зависит от класса `Animal`. Он зависит от его "интерфейса". Класс `Cat` "знает" о методах `Animal`. В классе `Animal` метод `makeSound` без каких-либо аргуметов. Именно поэтому нам не удается переопределить метод и указать аргумент `numberOfSounds`.

## Задание 3.

```java
/*
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.10</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version>
</dependency>
*/

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Создаем объект ObjectMapper для парсинга JSON
        ObjectMapper objectMapper = new ObjectMapper();

        String jsonString = "{\"name\":\"John\", \"age\":30}";

        try {
            // Парсим JSON-строку в HashMap
            Map<String, Object> result = objectMapper.readValue(jsonString, HashMap.class);

            System.out.println("Name: " + result.get("name"));
        } catch (IOException e) {
            // Обработка ошибки парсинга
            e.printStackTrace();
        }

        try {
            String prettyJson = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(result);
            System.out.println("Pretty JSON: " + prettyJson);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### Вопрос:
Какие незримые механизмы логики могут проявиться тут?

### Ответ:
В этом коде есть несколько видов зависимостей:

1) Зависимость от библиотеки `Jackson (jackson-databind)`: Этот код использует класс `ObjectMapper` из библиотеки `Jackson` для работы с `JSON`, поэтому программа зависит от версии этой библиотеки. В примере указано две версии `jackson-databind` в `<dependency>`, что может вызвать конфликты, так как система может не определить, какую версию использовать (версии 2.9.10 и 2.12.5). Рекомендуется оставить только одну версию для избежания конфликтов.

2) Зависимость от конкретных классов `Jackson`: В коде напрямую вызывается `ObjectMapper`, что предполагает сильную зависимость от реализации библиотеки `Jackson`. Если библиотека будет заменена на другую для работы с `JSON`, код придется переделывать.

3) Взаимозависимость данных внутри программы: Код обрабатывает переменную `result` и пытается снова использовать её в виде `pretty JSON`. Если возникнет ошибка при первой попытке парсинга `jsonString`, переменная `result` не будет инициализирована, что может привести к `NullPointerException` во втором блоке `try`. Это пример зависимости, когда одна часть кода полагается на корректное выполнение предыдущей.

