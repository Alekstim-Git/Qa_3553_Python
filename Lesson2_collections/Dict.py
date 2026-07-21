books = {
    'Harry Potter and.....': 'J.K.Rowling',
    'To kill a mockingdird': 'Harper Lee'
}

print()
books1 = {                           # в set -> порядок элементов всегда случайный
    'Harry Potter and.....',
    'To kill a mockingdird'
}
print(books1)
print()

response = {
    'status': 'success',
    'user': {'id': 1, 'name': 'Maria'}
}
print(response['user']['name'])         # вытащили имя
print()

data = [1, 22, 3]
print(isinstance(data, list))        # метод показывает list ли это

value = 10                            # провер int-True или float-False лежит
print(isinstance(value, (int,)))
print()

team_ages = {                      # что стоит слева, то key / что справа, то value !!
    'Alex': 23,
    'Viki': 42,
    'Petr': 52
}
print(team_ages.keys())
print(team_ages.values())
print()

team_names = ['Alex', 'Viki', 'Petr']        # ZIP собирает словарь
team_numbers = [23, 43, 52]
team_ages = {name: age for name, age in zip(team_names, team_numbers)}
print(team_ages)
