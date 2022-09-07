# Реализуйте алгоритм перемешивания списка

import random
n = int(input('Введите колличество эл-в списка : '))

n_list = []

for i in range(n):
    n_list.append(random.randint(-n,n))
print(n_list)

random.shuffle(n_list)
print(n_list)