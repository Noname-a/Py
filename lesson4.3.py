a = [1, 1, 1, 2, 3, 4, 6, 2, 7, 2, 8, 4]

for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
        if count == 2:
            break
    if count == 1:
        print(i)
