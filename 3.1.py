n = int (input('Введите номер четверти: '))

print ('Диапазон этой четверти: ')
if n == 1:
    print ('0 <= x < +00')
    print ('0 <= y < +00')
if n == 2:
    print ('-00 < x <= 0')
    print ('0 <= y < +00')
if n == 3:
    print ('-00 < x <= 0')
    print ('-00 < y <= 0')
if n == 4:
    print ('0 <= x < +00')
    print ('-00 < y <= 0')
