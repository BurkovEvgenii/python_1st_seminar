# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите цифру, которая обозначает день недели: ')
day_week =int(input())
if day_week > 0 and day_week < 6:
    print('Workday')
elif day_week > 5 and day_week <8:
    print('Freeday')
else: 
    print('Write a day number!')
