name = 'Alice'
age = 30

formatted_string = f'Hello ma name is {name} and I am {age} years old'
print(formatted_string)
# ********************************************

# find() -принимает сабстроку индекс начало и индекс конца

s = 'AblakadabraAbrakadabra'
str = 'bra'
print(s.find(str))  # s.-возьми перв строку и найди (str)-сабстроку
# находит Индекс ПЕРВОГО совпадения.
# ***********
print(s.rfind(str))
# находит Индекс ПОСЛЕДНЕГО совпадения.
# **************
print(s.find('BLA'))  # если нет совпад, то выдаст [-1]
# ******************
# count(sub,start,end])
print(s.count(str))  # посчитает [bra] в строке
print(s.count(str, 9))  # начинает искать с ИНДе 9
print(s.count(str, 4, 15))  # ищет с 4 По 14 ИНДЕКса
# ***********************************
# методы, которые преобразуют символы строки в Верх и Нижний регистры

# str.upper() -> в Верхний
# str.lower() -> в Нижний

s = 'AblakadabraAbrakadabra'
print(s.upper())
print(s.lower())
print(s)
print('*************************************')
print()
# split() метод разрезает строку по заданному делителю и возвращ список
s = 'Cat, Dog,Hamster Rabbit, Pig'
print(s.split())  # разбивает по Пробелу
print(s.split(','))  # разбивает по Запятой
# ***********************************************

# rjust()  # - выравнивает строку по правому краю, дописывая
# слева нужные символы (по умолчанию — пробелы) до заданной длины.
# ljust()  # - выравнивает строку по левому краю, дописывая
# символы (по умолчанию — пробелы) справа, чтобы подогнать строку под нужную длину.

s = 'Hi!'
print(s.rjust(10, '*'))
print(s.ljust(10, '*'))
print()

test = ['Login', 'Cart', 'API']  # пишет слово, отсчитывает символы с нач слова и на 16й ставит Ок
for t in test:
    print(t.ljust(15), 'Ok')
print()

order = '125'
print(order.rjust(8, '0'))
# ***********************************
print()

s = 'AblakadabraAbrakadabra'
print(s.isalpha())  # если только буквы в строке, то даст True
print(s.isdigit())  # если только цифры в строке, то даст True
# ************************************

# index()
text = 'QA automation with Python'
pos = text.index('automation')
print(pos)

# pos =text.index('automation', 10)   #ищи где начинается с 10 символа. Но такого нет и даст ошибку.
# print(pos)
# ************************************

# replace() #метод, который заменяет одну суб-строку на другую внутри текста.
text = 'I like Java'
print(text.replace('Java', 'Python'))
print()
text = '2026-07-03'
new_text = text.replace('-', '/')
print(text)
print(new_text)
