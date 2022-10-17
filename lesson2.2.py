from math import factorial

n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)