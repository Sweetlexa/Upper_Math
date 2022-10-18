import math
a = input('Введите координаты вектора через пробел: ').split()
a = list(map(int,a))
i = 0
n = 0
for el in a:
    if i < len(a):
        n = n + a[i]**2
        i = i + 1
l = math.sqrt(n)
print('Длина вектора: ', l)
