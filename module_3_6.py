data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(data_structure):
    sum = 0
    for index in data_structure:
        if isinstance(index, int) or isinstance(index, float):
            sum += index
        elif isinstance(index, str):
            sum += len(index)

        elif isinstance(index, dict):
            for key, value in index.items():
                if isinstance(key, str):
                    sum += len(key)
                if isinstance(value, (int, str)):
                    if isinstance(value, int):
                        sum += value
                    elif isinstance(value, str):
                        sum += len(value)
        elif isinstance(index, (list, tuple, set)):
            sum += calculate_structure_sum(index)

    return sum


result = calculate_structure_sum(data_structure)

print(result)
