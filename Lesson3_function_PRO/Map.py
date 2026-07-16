# map() — это встроенная функция в Python, которая позволяет применить другую функцию
# к каждому элементу списка (или любого другого перечня данных) без использования циклов for.

# Она берёт каждый элемент по очереди, «прогоняет» его через указанную функцию и выдаёт
# изменённый результат.

numbers = [1,2,3,4,5]
squared = map(lambda x: x ** 2, numbers)
print(squared)
print(list(squared))
print()


def to_upper(s):
    return s.upper()
statuses = ['passed','failed','skipped']
upper_statuses = list(map(to_upper,statuses))
print(upper_statuses)