

Проект: Натаскер.

#  Как сделать простой опрос на Python и TynyDB (CLI) 

## Простой проходкой по вопросам 

Фаил make.py

### Подключаем базовые модули

``` python
import os # доступ к операциям ос (очистка вывода консоли)
```

### Подключаем модули для работы базой

```Python
from tinydb import *
from tinydb.operations import *
from tinydb import Query

```

### Иницилизируем базу  и возможность поиска и обьект 

```python
dbtb = TinyDB('./db/tb.json')
Bl= Query()
tb={}
```



### Задаем вопрос

#### Создаем функцию 

```python
def ask(qu,key){
    ans = input(qu) # вывод запроса с подсказкой
    tb[key]=ans # запись ответа в соответвующий ключ
}
```

##### Задаем  вопросы + очищаем экран

```python
ask("Имя пользователя","name")
os.system('cls||clear')  

ask("Тема","theme")
os.system('cls||clear') 

ask("Хочу или надо","xn")
os.system('cls||clear')

ask("Настроение на дело","mood")
os.system('cls||clear') 

ask("Продолжительность в минутах","delta")
os.system('cls||clear') 

ask("Дата начала dd-mm-yy ","date")
ask("Время начала hh:mm ","theme")
os.system('cls||clear') 

```



### Добавляем в базу 

```python
dbtb.insert(tb)
```



## Итог

В базу сделана запись с ответами на вопросы, c заданными ключами.

 