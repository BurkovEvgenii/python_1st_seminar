# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Write a quarter num:')
q_num = int(input())
if q_num == 0 or q_num >= 5:
    print('Invalid quarter number')
else:
    print('Great, possible coordinates: ')

if q_num == 1:
    for i in range(1, 11):
        print('[Y:' + str(i) + ']', end =' ')
        print('[X:' + str(i) + ']', end =' ')
elif q_num == 2:
    for i in range(1, 11):
        print('[Y:' + str(i) + ']', end =' ')
        print('[X:' + str(-i) + ']', end =' ')
elif q_num == 3:
    for i in range(1, 11):
        print('[Y:' + str(-i) + ']', end =' ')
        print('[X:' + str(-i) + ']', end =' ')
elif q_num == 4:
    for i in range(1, 11):
        print('[Y:' + str(-i) + ']', end =' ')
        print('[X:' + str(i) + ']', end =' ')



