# (lambda) в Python — это анонимная (не имеющая имени) функция, которую можно записать
# в одну строку кода. Она используется для простых операций, когда полноценную
# функцию через def создавать нет смысла или нужно передать простое действие
# как аргумент в другую функцию.

# d lambda ни когда нельзя написать несколько строк


def double(x):
    return x * 2

double_lambda = lambda x: x * 2

print(double(5))

print(double_lambda(5))
print()


add=lambda a,b: a+b
print(add(3,4))
print()

is_even = lambda n:n%2 ==0
print(is_even(10))
print(is_even(7))

