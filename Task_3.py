# Задайте список из k чисел последовательности 
# (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Введите K : '))

nums = []
import math

for i in range(1, k+1):
    num = ((1 + 1/i)**i)
    num = math.floor(num*100)/100
    nums.append(num)

print(nums)

sum = 0

for i in range(k):
    sum = sum + nums[i]
sum = math.floor(sum*100)/100
print(f'Сумма всех члеов списка = {sum}')