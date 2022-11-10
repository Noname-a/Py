#В общем, когда пытался на русском написать текстовый файл, то выдовал ошибку, пытался в инете найти, но там решения не нашел

with open("words.txt") as a:
    txt = a.read()
   
print(f"Исходный текст: {txt}")
find_txt = "abv"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

with open("words_ispravleno.txt", 'w') as a:
    a.write(f'Ispravleno: {" ".join(lst)}')

