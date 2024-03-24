import random
import sys

data = {}
try:
    with open("rooms.txt", "r", encoding="UTF-8") as file:
        for line in file:
            name, room = line.strip().split("-")
            data[name] = room
except FileNotFoundError as e:
    print("Мы видимся с вами впервые!")

prog_name = input("Введите ваше имя: ")

print("Добрый день!")
print(f"Введите пары в виде \"Имя-Номер\"")
lines = map(str, sys.stdin)

for line in lines:
    name, room = line.strip().split("-")
    data[name] = room
if prog_name in data:
    print(f"Ваш номер: {data[prog_name]}")
else:
    keys = [i for i in data.keys()]
    print(f"Ваш номер: {data[keys[random.randint(0, len(keys) - 1)]]}")
with open("rooms.txt", "w", encoding="UTF-8") as file:
    file.writelines([f"{k}-{v}\n" for k, v in data.items()])
