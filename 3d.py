# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30)


print('Введите число: ')
num = int(input())
if num % 5 == 0 or num % 10 == 0 or num % 15 == 0 or num % 30 != 0:
    print('True')
else:
    print('False')