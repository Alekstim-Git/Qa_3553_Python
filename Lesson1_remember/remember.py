age = 25
name = 'Ivan'

'''
int - целые числа
float - дробные
str - строки
bool - логический
'''
said = "She said 'Hello'"
print(said)

my_string = '''This is a multy-line string. 
We've wrapped the text to the next line'''
print(my_string)

raw_sting = r"C:\Program Files\Marii\Python"  # что бы воспринимал \-> как строку
print(raw_sting)

s1 = "Hello word"
print(type(s1))  # метод type -> выдаёт характеристику строки.
s2 = 5
print(type(s2))
s3 = False
s4 = 3.8
print(type(s4))

s1 = 'Zeleno'  # склеивание строк
s2 = 'glazka'
s3 = s1 + s2
print(s3)

s1 = 'Zeleno'  # склеивание наоборот
s2 = 'glazka'
s3 = s2 + s1
print(s3)

# join () метод
words = ["Hello", "World", "and", "Python"]
result = " ".join(words)
print(result)

st = 'ab' * 7  # умножение ab
print(st)

st = 35 * '*'  # умножение *
print(st)

s1 = 'Vasya Pupkin'  # ищет есть ли Vasya в str.1
s2 = 'Vasya'
if s2 in s1:
    print('User Vasya is in our database')
else:
    print('User Vasya not in the DB')

st = 'a'
if st == 'a' or st == 'b' or st == 'c' or st == 'd':
    print('Yes')  # ищет на совпадения

if st in 'abcd':  # так удобнее запросить на совпадения
    print('Yes')

# ***************************************/
# длина строки
# len()
ln = len('Zelenoglazka')
print(ln)

s1 = 'Zelenoglazka'  # можно и так написать
print(len(s1))

# ***************************************
# доступ по индексу

# P Y T H O N
# 0 1 2 3 4 5
st = 'Python'
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])

# P  Y  T  H  O  N
# -6 -5 -4 -3 -2 -1    # предусмотренная альтернатива нумерации
st = 'Python'
print(st[-6])
print(st[-5])
print(st[-4])
print(st[-3])
print(st[-2])
print(st[-1])
# **************************
# my_string[start:end]
# P Y T H O N
# 0 1 2 3 4 5
print(st[0:3])
print(st[2:5])
print(st[4:6])

my_string = 'Hello World!'  # выпишет каждый второй символ
every_second_char = my_string[::2]
print(every_second_char)

from_second = my_string[1::2]
print(from_second)

my_substring = my_string[1:10:3]
print(my_substring)

reversed_string = my_string[::-1]
print(reversed_string)
