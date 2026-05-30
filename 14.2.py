class Restoran:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}" )
        print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print(f'{self.restaurant_name} открыт!')

class IceCreamStand(Restoran):
    def __init__(self, restaurant_name, cuisine_type, flavors,
                 location, workhours, icecreamtypes):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.workhours = workhours
        self.icecreamtypes = icecreamtypes
    def flavors_list(self,flavors):
        if flavors in self.flavors:
            print("Такое мороженное есть")
        else:
            self.flavors.append(flavors)
        print(f'Список мороженного в продаже: {self.flavors}')
    def addfl(self, flavors):
        if not flavors:
            ('Название не может бть пустым')
            return
        if flavors in self.flavors:
            print(f'Вкус {flavors} уже есть')
        else:
            self.flavors.append(flavors)
            print(f'Вкус {flavors} Добавлен')
    def deletefl(self, flavors):
        if flavors in self.flavors:
            self.flavors.remove(flavors)
            print(f'Вкус {flavors} удален')
        else:
            print(f'Вкус {flavor} не найден')
    def types(self, icecreamtypes ):
        print('типы мороженного')
        for i in self.icecreamtypes:
            print(f'{i}')
    def info(self):
        print(f'Локация {self.location}')
        print(f'Время работы {self.workhours}')
    def proverka(self, flavors):
        if flavors in self.flavors:
            print('Такой вкус уже есть')
        else:
            print('Такого вкуса нет')
NewIceCreamStand = IceCreamStand("Стаканчик","Русская", ["Шоколадное", "Клубничное"], 'Васильевский остров', '10:00 - 20:00', ['На палочвке', 'Рожок', 'Мягкое'])
print(f'Название: {NewIceCreamStand.restaurant_name}')
print(f'Тип кухни: {NewIceCreamStand.cuisine_type}')
NewIceCreamStand.flavors_list("Шоколадное")
NewIceCreamStand.flavors_list("Пломбир")
print(f'Локация: {NewIceCreamStand.location}')
print(f'Время работы: {NewIceCreamStand.workhours}')
NewIceCreamStand.deletefl('Шоколадное')
NewIceCreamStand.addfl('Фисташковое')
print(f'Вкусы {NewIceCreamStand.flavors}')
NewIceCreamStand.proverka('Сырное')

