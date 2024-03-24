import pymorphy3

morph_ru = pymorphy3.MorphAnalyzer(lang='ru')

data = (
    ("Пётр", "Иванов", "Василиевич"),
    ("Иван", "Пёторов", "Василиевич"),
    ("Василий", "Пёторов", "Иванович"),
    ("Андрей", "Выдра", "Михаилович"),
    ("Дмитрий", "Примеров", "Тестович"),
    ("Дмитрий", "Викторов", "Алексеевич"),
    ("Александр", "Недвижимов", "Ильич")
)

inputs = (
    "Петр Васильевич Иванов",
    "Иванов Петр Васильевич",
    "Петр Иванов",
    "иванов Петр",
    "Петр",
    "михалыч",
    "Выдра",
    "выдр",
    "Ивано",
    "движ",
    "ор",
    "Андр",
    "Примеров Дмитрий",
    "Иванов Васильевич",
    "Андрей Пёторов"
)

for inp in inputs:
    user_input = inp.strip()
    points = [0 for i in range(len(data))]
    for word in user_input.split():
        best_parse = morph_ru.parse(word)[0]
        tag = best_parse.tag
        idx = -1
        if best_parse.score > 0.5:
            if "Name" in tag:
                idx = 0
            elif "Patr" in tag:
                idx = 2
            elif "Surn" in tag:
                idx = 1

        for i, item in enumerate(data):
            if idx == -1:
                for element in item:
                    points[i] += len(word) / len(element) if word.lower() in element.lower() else 0
                continue
            if best_parse.normal_form.lower() == item[idx].lower():
                points[i] += best_parse.score

    idx = 0
    max_points = 0
    for i, point in enumerate(points):
        if point > max_points:
            max_points = point
            idx = i

    print("______________________________")
    print("Для строки -", user_input)
    if max_points > 0:
        print("Совпадение найдено, данные о пользователе: ", data[idx])
    else:
        print("Совпадения не обнаружено")
