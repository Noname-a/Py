col = int(input("Введите количество элементов: "))
list_1 = []

for _ in range(col):
    num = input()
    list_1.append(num)

minn = 1
maxx = 0
print("Ваш список: ", list_1)

for el in list_1:
    if "." in str(el):
        dr = str(el).split('.')[1] 
        if float('0.' + dr) > maxx:
            maxx = float('0.' + dr)
        if float('0.' + dr) < minn:
            minn = float('0.' + dr)

print("Разница между max и min: ", maxx - minn)