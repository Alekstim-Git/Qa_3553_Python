import csv

with open('users_1.csv','w', encoding='utf-8', newline='') as file:
    writer =csv.writer(file)

    writer.writerow(['name','email','role'])
    writer.writerow(['Anna', 'anna@gmail.com', 'admin'])
    writer.writerow(['Bob', 'bob@gmail.com', 'user'])


with open('users_1.csv') as file:
    reader=csv.reader(file)
    print(type(reader))              # type - показывает, с каким типом данных я работаю.

    for row in reader:
        print(row)          #row -общепринятый стандарт переменной при работе с табл. (можно хоть line)

print()
with open('users_1.csv','r',encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)
        print(row['name'],'-', row['role'])