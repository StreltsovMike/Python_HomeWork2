# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.


from random import Random, randint

n = int(input('Введите N : '))

n_list = []

for i in range(n):
    n_list.append(randint(-n,n))
print(n_list)

from operator import le
left, right = (int(i) for i in input('Введите через пробел позиции : ').split()) #input('Введите через пробел позиции : ').split()

product_of_numbers = 1
for i in range(left-1, right):
    product_of_numbers = product_of_numbers * n_list[i]

print(f'Произведение чисел на указанном промежутке = {product_of_numbers}')