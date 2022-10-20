from traceback import print_list


col = int(input("Введите количество элементов: "))
list_1 = []
summa = 0

for _ in range(col):
    num = int(input())
    list_1.append(num)

print("Ваш список: ", list_1)

for index in range(1, col, 2):
    summa += list_1[index]

print("Сумма элементов на нечетных позициях:", summa)