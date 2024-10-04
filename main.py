class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor < 1 or new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        print(self.numbers_of_floors)

    def __str__(self):
        print(f"Название: {self.name}, кол-во этажей:{self.numbers_of_floors}")

h1 = House('ЖК Горьковский', 18)
h2 = House('Домик в деревне', 2)
h1.__str__()
h2.__str__()
h1.__len__()
h2.__len__()