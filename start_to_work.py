#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

print ('Введите первое число: ')
a = int(input())
print ('Введите второе число: ')
b = int(input())

if a ** b / a == a:
     print('Является квадратом')
else:
     print('Не является квадратом')    
if b / a == a:
    print('Является квадратом')
else:
    print('Не является квадратом')

list = [78, 55, 95, 90, 2]
max_n = list[0]
for i in list:
    if i > max_n:
        max_n = i
print(max_n)



