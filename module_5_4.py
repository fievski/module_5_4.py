class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        o = super().__new__(cls)
        cls.houses_history.append(house_name)
        return o

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Пристройский', 18)
print(House.houses_history)
h2 = House('ЖК Сарай на даче', 2)
print(House.houses_history)
h3 = House('ЖК Отличные дома', 1)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

# Метод new и класс object
# class User:
#     __instance__ = None
#     def __new__(cls, *args, **kwargs):
#         print('Я в нью')
#         if cls.__instance__ is None:
#             cls.__instance__ = super().__new__(cls)
#         return cls.__instance__
#
#     def __init__(self, *args, **kwargs):
#         print('Я в ините')
#         self.args = args
#         for key, values in kwargs.items():
#             setattr(self, key, values)

# other = [1, 2 ,3]
# user = {'name': 'Sam', 'age': 25, 'gender': 'male'}
#
# user1 = User(*other, **user)
# print(user1.args)
# print(user1.name)
# print(user1.age)
# print(user1.gender)


