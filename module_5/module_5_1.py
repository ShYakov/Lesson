class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')
    def __len__(self):
        return self.number_of_floor
    def __str__(self):
        return self.name



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(f'Название: {h1.name}, кол-во этажей: {len(h1)}')
print(f'Название: {h2.name}, кол-во этажей: {len(h2)}')
print(len(h1))
print(len(h2))












