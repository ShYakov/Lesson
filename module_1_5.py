immutable_var = (1, 2, 'String')
print(immutable_var)
# immutable_var [0] = 33
print(immutable_var) # кортежи не поддерживают изменение элементов. TypeError: 'tuple' object does not support item assignment
mutable_list = [1, 2, 'String']
mutable_list [1] = 'Print'
print(mutable_list)