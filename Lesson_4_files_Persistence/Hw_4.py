import csv

# № 1
def save_shopping_list(items):
    with open('shopping.txt', 'w', encoding='utf-8') as file:
        for item in items:
            file.write(f"{item}\n")

items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]
save_shopping_list(items)

# № 2
def read_students(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student: {row['name']} ({row['age']})")
read_students('students.csv')

# № 3
import json

def save_profile(name, age, city):
    profile = {
        'name': name,
        'age':age,
        'city': city
    }
    with open('profile.json', 'w', encoding='utf-8') as file:
        json.dump(profile, file, indent=2, ensure_ascii=False)

save_profile('Maria', 30, 'Haifa')