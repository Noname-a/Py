a = int(input("Введите число: "))
list_1 = [0] * (a * 2 + 1)
list_1[a + 1] = 1

for index in range(a + 2, a * 2 + 1):
    list_1[index] = list_1[index - 1] + list_1[index - 2]

for index in range(a, -1, -1):
    list_1[index] = list_1[index + 2] - list_1[index + 1]

print(list_1)