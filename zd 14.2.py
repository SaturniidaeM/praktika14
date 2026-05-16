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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, work_hours, icecreamtypes):
        super().__init__(restaurant_name, cuisine_type)
        self.location = location
        self.work_hours = work.hours
        self.flavors = []
        self.icecreamtypes = {

        }
    def flavors_list(self,flavors):
        if flavors in self.flavors:
            print("Такое мороженное есть")
        else:
            self.flavors.append(flavors)
        print(f'Список мороженного в продаже: {self.flavors}')
    def loc_hour(self:
        print(f'Местоположение: {self.location}')
        pri