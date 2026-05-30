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
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def flavors_list(self,flavors):
        if flavors in self.flavors:
            print("Такое мороженное есть")
        else:
            self.flavors.append(flavors)
        print(f'Список мороженного в продаже: {self.flavors}')

NewIceCreamStand = IceCreamStand("Стаканчик","Русская", ["Шоколадное", "Клубничное"] )
print(f'Название: {NewIceCreamStand.restaurant_name}')
print(f'Тип кухни: {NewIceCreamStand.cuisine_type}')
NewIceCreamStand.flavors_list("Шоколадное")
NewIceCreamStand.flavors_list("Пломбир")

