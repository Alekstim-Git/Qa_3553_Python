from Lesson1_remember.remember import my_string

numbers_tuple = (1, 2, 3, 4, 5, 3, 9, 7)
my_tuple = ([1, 2, 3], ['a', 'b', 'c'])

first_element = numbers_tuple[0]  # 0 -> это индекс

nested_tuple = (1, 2, (3, 4), 5)  # (3,4) -> это один-единственный неделимый элемент, под общим индексом [2].
print(nested_tuple[2])
print(nested_tuple[2][1])  # распечат что в индексе [2](как отд элемент) под инд [1]
print()

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6)
print(tuple1 == tuple2)  # печатает True или False
print(tuple1 == tuple3)
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)
print(33 in my_tuple)
print()

for el in my_tuple:
    print(el)

i = 0
while i < len(my_tuple):  # берёт длину кортежа и увеличивает на +1, пока условие верно.
    print(my_tuple[i])
    i += 1

del my_tuple
# # print(my_tuple)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
conc_tuple = tuple1 + tuple2
print(conc_tuple)

my_tuple = (1, 2, 3, 4, 5)
lenght_of_tuple = len(my_tuple)
print(lenght_of_tuple)

sum_of_elements = sum(my_tuple)  # сумма цифр кортежа
print(sum_of_elements)

print()
max_element = max(my_tuple)
min_element = min(my_tuple)
print(max_element)
print(min_element)

my_tuple1 = ()
print(len(my_tuple1))  # как реагирует на пустое значение
print(sum(my_tuple1))
# print(max(my_tuple1))
# print(min(my_tuple1))

original_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
sorted_tuple = tuple(sorted(original_tuple))  # сортирует цифры в кортеже
print('original:', original_tuple)
print('sorted:', sorted_tuple)

sub_tuple = original_tuple[3:7]  # выбрал по индексу (с 3 до 7, но не включая 7)
print(sub_tuple)

my_tuple = list(original_tuple)  # преобразовали в список
print(my_tuple)

my_string = ''.join(map(str, original_tuple))  # преобразование в строку
print(my_string)
print()

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list[2] = 10  # заменили в инд2 элемент в кортеже!
updated_tuple = tuple(my_list)
print('Original tuple:', my_tuple)
print('Updated tuple:', updated_tuple)
print()
