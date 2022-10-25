n = float(input("Введите число, которое хотите округлить: "))
d = float(input("Введите число, по которому хотите округлить: "))
if d == 1:
    print(int(n))
else:
    d = str(d)
    d = d.split('.')
    d = len(d[1])
    print(round(n, d))