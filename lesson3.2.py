col = int(input("Введите количество элементов: "))
list_1 = []

for _ in range(col):
    num = int(input())
    list_1.append(num)
    list_2 = []

print("Ваш список: ", list_1)

for index in range((col - 1) // 2 + 1):
    num1 = list_1[index]
    num2 = list_1[col - index - 1]
    list_2.append(num1 * num2)

print("Произведение пар чисел:", list_2)