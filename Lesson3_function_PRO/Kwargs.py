# kwargs -
# (сокращение от keyword arguments — «именованные аргументы» 'Anna' и тд) — это инструмент,
# который позволяет передавать в функцию любое количество именованных
# аргументов (в формате ключ = значение).

# Если обычный *args собирает все переданные данные в кортеж (tuple), то **kwargs
# (с двумя звёздочками) упаковывает их в словарь (dict).


def print_config(**kwargs):
    print()
    print(type(kwargs), kwargs)
    return kwargs
print(print_config(browser='Chrome', headless=True, timeout=30))
print(print_config())  # передаст пустой словарь


def create_user(**data):
    return data
user = create_user(name='Anna', role='admin')
print()
print(user)



def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
example(1, 2,3,4, name='Anna')
