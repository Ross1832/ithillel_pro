books_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99],
]

result = list(
    map(lambda temp: tuple([temp[0], round(temp[2] * temp[3] + 10 if temp[2] * temp[3] <= 100 else temp[2] * temp[3], 2)]),
        books_list))

print(result)
