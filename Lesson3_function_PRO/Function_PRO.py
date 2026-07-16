from venv import create


def greet(name):
    return f'Hi, {name}!'


result = greet("Maria")
print(result)


# собирает из полученных данных структурированную карточку пользователя (словарь dict с ключами 'name' и 'role').
def create_user(name, role='user'):
    return {
        'name': name,
        'role': role
    }


print(create_user('Maria'))
print(create_user('Maria', 'admin'))
print()


def calculate_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)


print(calculate_discount(1000))
print(calculate_discount(1000, 25))


# по умолчанию ставит 10. Либо устанавливаешь значение discount сам.


# Как добавить элемент в список внутри функции так, чтобы код не сломался и не смешал данные от разных запусков
def add_test_result(name, results=None):  # пишем None !!, так как писать results=[] в скобках ОПАСНО!
    if results is None:
        results = []  # создаем новый чистый список (внутри функции это безопасно)
    results.append(name)
    return results


# print(add_test_result('test_login'))
print(add_test_result('test_logout'))


# позиционный вызов. Важен порядок при внесении данных.
def create_user_1(username, email, role):
    return f'{username} ({email:}) - {role}'


print(create_user_1('Maria', 'maria@gmail.com', 'admin'))

# будет тоже самое согласно форме
print(create_user_1(role='admin', username='Maria', email='maria@gmail.com', ))
