def avg_kg():
    avg = 0
    counter = 0
    with open('hw.csv', 'r') as file:
        for i in file.readlines()[1:-1]:
            avg += float(i.replace('\n', '').split()[2])
            counter += 1
    res = round(avg/counter*0.453592, 2)
    return res


def avg_height():
    avg = 0
    counter = 0
    with open('hw.csv', 'r') as file:
        for i in file.readlines()[1:-1]:
            avg += float(i.replace(',', '').split()[1])
            counter += 1
    res = round(avg/counter*2.54, 2)
    return res


