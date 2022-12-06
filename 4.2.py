# Задача №3

import csv

with open('sales.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    del table[0]                                        # удаляем заголовок
    table.sort(key=lambda item: int(item[1]))
    for line in table[:5]:
        print(line)