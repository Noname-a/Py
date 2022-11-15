hi = 'Привет, {}!'

incorrect_staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for correct_staff in incorrect_staff:
    print(hi.format(correct_staff.split()[-1].title()))