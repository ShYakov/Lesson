# Распаковка
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(99, 98, False)
print_params(25, [1, 2, 3])
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
value_list = [15, 'ятелефон', True]
values_dict = {'a': 'тут один', 'b': 99.99, 'c': 'Действительно'}
print_params(*value_list)
print_params(**values_dict)  # ошибка, ключевые слова должны быть строками

# Распаковка + отдельные параметры
value_list2 = [54.32, 'Строка']
print_params(*value_list2, 42)
