# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
xyz = [3, 5, 7]
left = not (xyz[0] or xyz[1] or xyz[2])
right = not xyz[0] and not xyz[1] and not xyz[2]
if left == right:
    print('True')
else:
    print('False')
