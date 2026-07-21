# dumps()
#             #-> Он берет объект Python (например, словарь или список) и конвертирует
# (сериализует) его в обычную строку формата JSON.
import json

# loads()
              #->  (сокращение от "load string" — загрузить из строки) — это противоположность метода
# dumps(). Он берет текстовую строку в формате JSON и конвертирует (десериализует) её обратно
# в объект Python (в словарь или список).

# dump()
              #-> (без буквы s на конце) — это метод модуля json, который берет объект Python (словарь или список)
# и сразу записывает его в файл на жестком диске в формате JSON.

# load()
              #->  (без буквы s на конце) — это метод модуля json, который читает данные из
# открытого JSON-файла и автоматически превращает их в объект Python (обычно в словарь или список).
#Он работает в паре с контекстным менеджером with open() в режиме чтения ('r').

user = {'username':'Egor', 'age':30, 'is_admin':True}   # <- это словарь!

json_string = json.dumps(user)   # словарь превращаем в строку!
print(json_string)
print(type(json_string))


user = json.loads(json_string)  # словарь превращаем в файл Python!
print()
print(user)
print(type(user))
print(user['username'])


test_config = {
    'base_url':'https://api.example.com',
    'timeout': 10,
    'retries':3
}

with open('config.json', 'w', encoding='utf-8') as file:
    json.dump(test_config,file, indent = 2,ensure_ascii=False)

with open('config.json', 'r', encoding='utf-8') as file:
    loaded_config=json.load(file)

    print(loaded_config)
    print(loaded_config['base_url'])
