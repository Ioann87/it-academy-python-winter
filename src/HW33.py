# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

lst = ['a', 'b', 'c']
tup_lst = tuple(lst)
print(tup_lst, type(tup_lst))
tup = ('a', 'b', 'c')
lst_tup = list(tup)
print(lst_tup, type(lst_tup))
a, b, c = 'a', '2', 'python'
print(a, b, c)
tupl = ([1, 2, 3],)
print(len(tupl), tupl)
for element in tupl[0]:
    print(element)
