import math

x1 = float(input('Введите точку x1: '))
y1 = float(input('Введите точку y1: '))
x2 = float(input('Введите точку x2: '))
y2 = float(input('Введите точку y2: '))

c = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(round(c, 2))

