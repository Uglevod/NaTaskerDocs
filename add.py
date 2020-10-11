import os # доступ к операциям ос (очистка вывода консоли)
from tinydb import *
from tinydb.operations import *
from tinydb import Query

dbtb = TinyDB('./dbtb.json')
Bl= Query()
tb={}

def ask(qu,ky):
    ans = input(qu) # вывод запроса с подсказкой
    tb[ky]=ans # запись ответа в соответвующий ключ


ask("Имя пользователя ","name")
os.system('cls||clear')

ask("Тема ","theme")
os.system('cls||clear')

ask("Хочу или надо ","xn")
os.system('cls||clear')

ask("Настроение на дело ","mood")
os.system('cls||clear')

ask("Продолжительность в минутах ","delta")
os.system('cls||clear')

ask("Дата начала dd-mm-yy ","date")
ask("Время начала hh:mm ","time")
os.system('cls||clear')

dbtb.insert(tb)
