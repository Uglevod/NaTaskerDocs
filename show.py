import os # доступ к операциям ос (очистка вывода консоли)

from tinydb import *
from tinydb.operations import *
from tinydb import Query

from datetime import *

dbtb = TinyDB('./dbtb.json')
Tb= Query()

for it in dbtb.all():
    print(it.doc_id, it['name'],it['theme'],it['date'],it['time'],it['delta'],it['mood'],it['xn'] )

ch=input(" >")

os.system('cls||clear')

res = dbtb.get(doc_id=int(ch))

print (res['theme'] ,end=" ")
print (res['date']  ,end=" ")
print (res['time']  ,end=" ")
print (res['mood'])

a=datetime.strptime(res["date"]+" "+res["time"], "%d-%m-%y %H:%M") # создание обьекта время
dt=timedelta(minutes=int(res["delta"])) # обьект тайм дельта в минутах
b=datetime.now() # момент времени соответвующий сейчас
c=a+dt # момент времени окончания интервала
ba=b-a # удалим из настоящего момента время до начала интервала оставив то что прошло
pro= (100*ba.total_seconds())/dt.total_seconds() # процент времени который прошел
print ("%",pro)
print ("Окончание",c)
