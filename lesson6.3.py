list = [57.8, 46.51, 97, 66, 19.48, 83, 33.11, 55, 7.77, 49]

store_id = id(list)
print(f"{'a':-^79}")
end_word: str = ", "

for i, num in enumerate(list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)


print(f"{'b':-^79}")
print(f"id перед сортировкой {store_id}")
list.sort()
print(list)
print(f"id после сортировки {id(list)}")

print(f"{'c':-^79}")

copy_of_list = list.copy()
copy_of_list.sort(reverse=True)

print(copy_of_list)
print(store_id)
print(id(copy_of_list))


print(f"{'d':-^79}")
print("Цены пяти самых дорогих товаров", list[-5:])