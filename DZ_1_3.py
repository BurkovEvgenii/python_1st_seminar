# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Enter a X point: ')
X = int(input())
print('Enter a Y point: ')
Y = int(input())
if X == 0 or Y == 0:
    print('Write number more then 0!')
else:
    print('Great,')

if Y > 0 and X > 0:
    print('1st quarter!')
elif Y > 0 and X < 0:
    print('2nd quarter!')
elif Y < 0 and X < 0:
    print('3rd quarter!')
elif Y < 0 and X > 0:
    print('4th quarter!')


