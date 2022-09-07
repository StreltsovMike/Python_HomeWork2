# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N

n = int(input('Введите число N : '))
 
fact = []
product_of_numbers = 1

for i in range(1, n+1):
    product_of_numbers = product_of_numbers * i
    fact.append(product_of_numbers)

print(fact)