# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
import collections

lst = [1, 2, 3, 4, 7, 'e', 4, 5, 2, 'e', 9, 6, 6, 8]
print([item for item, count in collections.Counter(lst).items() if count == 1])
