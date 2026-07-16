# Unpacking (распаковка) в Python — это процесс извлечения отдельных элементов из
# контейнера (списка, кортежа, # словаря или множества) и
# их быстрой записи в отдельные переменные.
#
# Вместо того чтобы доставать каждый элемент по индексу (как a = list[0]), ты можешь
# сделать это одной строчкой.  -> Собирает словарь.


def login(username,password):
    print(username,password)
data=['admin', '12345']
login(data[0],data[1])
login(*data)


user={
    'username':'admin',
    'password':'12345'
}
print()
login(**user)




