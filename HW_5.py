from random import randint
import random
import math
# Задание 1
x = random.randint(0, 36)
print('Выпало число: ', x)

x = randint(0,36)
if x % 2 == 0 and x != 0:
    print('Выпало число: ', x, 'Красный')
elif x == 0:
    print('Выпало число: 0')
else:
    print('Выпало число: ', x, 'Черный')

# Задание 2.1
k = 0
m = 0
n = 10000
l = 0
for i in range(0,n):   # Подбрасывание первой монетки
    x1 = random.uniform(0,10)
    if x1 < 5:
        k = k + 1
    if x1 > 5:
        m += 1
    x2 = random.uniform(0, 10) # Подбрасывание второй монетки
    if x2 < 5 and x1 < 5:  # Условие выпадения решка на обеих монетах (два независимых события произойдут одновременно)
        l = l + 1

p = k / n
q = m / n

p1 = l / n
print('Вероятность выпадения орла: ', p)
print('Вероятность выпадения решка: ', q)
print('Вероятность выпадения решка на обеих монетах: ', p1)
#Получается значение l~0.25, что и доказывает теорему произведения вероятностей.

# Задание 2.2
x1 = np.random.rand(9)
x2 = np.random.rand(9)
x3 = np.random.rand(9)
x4 = np.random.rand(9)
x5 = np.random.rand(9)
x6 = np.random.rand(9)
x7 = np.random.rand(9)
x8 = np.random.rand(9)
x9 = np.random.rand(9)
x10 = np.random.rand(9)
i = 0
x = []
for el in x1:
    if i < len(x1):
        x.append(x1[i]+ x2[i]+x3[i]+x4[i]+x5[i]+x6[i]+x7[i]+x8[i]+x9[i]+x10[i])
        i += 1
num_bins = 5
n, bins, patches = plt.hist(x,num_bins)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')

# Задание 3
p = 0.5 # Вероятность успеха
q = 0.5 #Вероятность неудачи
n = 579 # Количество испытаний
k = 100 # Количество успехов

# По формуле Бернули:
m = math.factorial(n)
l = math.factorial(k) * math.factorial(n-k)
c = m / l
P = c * p**k * q**(n-k)
print(P)


# Задание 4
import itertools
k=0
for p in itertools.permutations('0123',2):
    k +=1
    print(''.join(str(x) for x in p))
print("Число размещений", k)


n = 0
for p in itertools.combinations('01234',2):
    print(''.join(p))
    n +=1
print('Число сочетаний: ', n)

#Задание 5
x = []
y = []
i = 0
n = 0
while True:
    if i < 101 and n < 100:
        x.append(randint(n,n+10))
        y.append(x[i]*0.7 + ((0.24*randint(n,n+10))/0.52)+0.6)
        i += 1
        n += 1
    else:
        break
xcp = sum(x)/len(x)
ycp = sum(y)/len(y)

k = 0
s1 = []
s2 = []
s3 = []
s4 = []
while True:
    if k < len(x):
        s1.append(x[k] - xcp)
        s2.append(y[k] - ycp)
        s3.append((x[k] - xcp)**2)
        s4.append((y[k] - ycp)**2)
        k += 1
    else:
        break
a = 0
p1 = []
s5 = sum(s3)
s6 = sum(s4)
p2 = s5 * s6
q = math.sqrt(p2)
while True:
    if a < len(s1):
        p1.append(s1[a] * s2[a])
        a += 1
    else:
        break
q1 = sum(p1)
R = q1 / q  # Коэффициент корреляции
print(R)
