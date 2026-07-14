from tkinter.font import names

from Lesson1_remember.remember import words, result

empty_list = []
mixed = [2, 'orange', 4.22, True]

fruits = ['orange', 'peach', 'lemon']
print(fruits)
print(fruits[0])  # напечатается orange

fruits[1] = 'blueberry'  # меняем 'peach' на 'blueberry'
print(fruits)

print()
list1 = ['orange', 'peach']  # соединяет листы
list2 = ['shampoo', 'soap']
comb_list = list1 + list2
print(comb_list)
print()

fruits = ['orange', 'peach', 'lemon']
first, second, third = fruits  # сначала переменные, потом общая переменная
print(first)
print(second)
print(third)
print()

fruits = ['orange', 'peach', 'lemon']
for item in fruits:
    print(f'item in fruits:{item}')
    print()

correct_answers = ['orange', 'peach', 'lemon']
user_answers = ['orange', 'peach', 'lemon']
if correct_answers == user_answers:
    print('All answers are correct!')
else:
    print('Some answers are incorrect')
print(len(fruits))
print()
# ------------------------------------------------------
numbers = [12, 56, 94, 6]  # указ больш число и маленьк
print(max(numbers))
print(min(numbers))
print()

res = sorted(numbers)  # расставляет от меньшего к большему
print(res)

print(numbers)  #
print(sorted(numbers, reverse=True))  # разворачивает строку (от больш к меньш)
print(sorted(fruits, reverse=True))  # разворач слова по алфавиту
print()

word = 'python'
print(sorted(word))  # отсортировал по алфавиту
result = ''.join(sorted(word))  # собрал подряд, склеил сортировку
print(result)
print()

names = ['Aleksandr', 'Bob', 'Tom']
print(sorted(names))
print(sorted(names, key=len))  # взял по длине слова и алфавиту
print()

fruits = ['orange', 'peach', 'lemon']
fruits.append('orange')  # append --> добавляет всегда в хвост
print(fruits)

fruits.insert(1, 'apple')  # вставляет элемент по индексу
print(fruits)

first_peach_index = fruits.index('peach')  # показывает № индекса элемента
print(f"The first 'peach' was added to position:{first_peach_index}")
print()

fruits.remove('orange')  # удаляет элемент по значению. Если их два, то удалит первый.
print(fruits)

fruits.pop(2)  # удаляет элемент по значению индекса
print(fruits)
print()
numbers = [10, 20, 30]
deleted = numbers.pop(1)  # удаляет элемент по значению индекса, но возвращ его(показ)
print(deleted)
print(numbers)
print()

numbers.clear()  # удаляет всё из списка, возвращает пустой лист
print(numbers)
