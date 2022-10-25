def factorization(n):
    p = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d
        d += 1
    if n > 1:
        p.append(n)
    return p
 
a = factorization(int(input()))
b = []
a.reverse()
for i in a:
    if i not in b:
        print(f'{i}^{a.count(i)}')
        b.append(i)