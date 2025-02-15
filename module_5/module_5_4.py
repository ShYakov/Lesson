class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        isinstance = super().__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return isinstance
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __len__(self):
        return self.number_of_floor

    def __del__(self):
        print(f'{self.name} снес,но остается в истории')

h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)



# Удаление объектов

del h2

del h3



print(House.houses_history)








