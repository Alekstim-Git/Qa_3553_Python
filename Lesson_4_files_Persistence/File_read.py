with open('users.txt','w', encoding='utf-8') as file:
    file.write('tony\n')
    file.write('ivan\n')
    file.write('anna\n')

   # read() - читает весь файл целиком.
with open('users.txt','r', encoding='utf-8') as file:
    content=file.read()
print(content)
print(len(content))      # нашли длину строки / строк в символах
print()
   # readlines() -->

# — это метод, который считывает весь файл целиком и разбивает его
# на список строк.
# где каждый элемент - одна строка файла (строка в кавычках).

with open('users.txt','r', encoding='utf-8') as file:
    lines = file.readlines()
print(lines)
print()

for line in  lines:
    print(line.strip())    # strip - убирает символы лишние (\n)- к примеру.
print()

                      # этот метод более удобный (со strip):

with open('users.txt','r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
