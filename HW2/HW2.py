students = []

with open('src.txt', 'r') as file:
    f = file.readlines()
    for i in f:
        students.append(i.replace('\n', '').split())

sum_s = 0

with open('dest.txt', 'w') as file:
    for i in students:
        temp = [None] * 3
        temp[0] = i[1]
        temp[1] = f"{i[0][0]}."
        temp[2] = round(sum([int(i) for i in i[2:]]) / len(i[2:]), 2)
        decimal = int(str(temp[2])[::-1].find('.'))
        template_decimal2 = f"{temp[0]} {temp[1]} {str(temp[2]).rjust(20 - len(temp[0]), ' ')}"
        template_decimal1 = f"{temp[0]} {temp[1]} {str(temp[2]).rjust(20 - len(temp[0]) - 1, ' ')}"
        if temp[2] < 5 and decimal == 2:
            print(template_decimal2)
            file.write(template_decimal2 + '\n')
        elif temp[2] < 5 and decimal == 1:
            print(template_decimal1)
            file.write(template_decimal1 + '\n')
        elif decimal == 2:
            file.write(template_decimal2 + '\n')
        elif temp[2] >= 5 and decimal == 1:
            file.write(template_decimal1 + '\n')
        sum_s += temp[2]

print(f"\nСредний бал студентов: {round(sum_s/len(students), 2)}")