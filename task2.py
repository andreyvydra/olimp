min = 100
x, y = 0, 0
for x1 in range(1, 80):
    for x2 in range(1, 80):
        if x2 == 80 / x1:
            if max(x1, x2) < min:
                min = max(x1, x2)
                x = x1
                y = x2
print("Необходимое кол-во человек:", min)
print(f"{x} в первый день, {y} во второй день")