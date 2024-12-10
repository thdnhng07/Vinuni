class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = int(year)

    def display_info(self):
        return self.brand, self.model, self.year


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = int(num_doors)

    def display_info(self):
        return (*super().display_info(), self.num_doors)


class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = float(payload_capacity)

    def display_info(self):
        return (*super().display_info(), self.payload_capacity)


n = int(input())

for _ in range(n):
    data = input().split()
    vehicle_type = data[0]

    if vehicle_type == "Car":
        _, brand, model, year, num_doors = data
        car = Car(brand, model, year, num_doors)
        car_info = car.display_info()
        print(
            f"Brand: {car_info[0]}, Model: {car_info[1]}, Year: {car_info[2]}, Number of doors: {car_info[3]}"
        )
    elif vehicle_type == "Truck":
        _, brand, model, year, payload_capacity = data
        truck = Truck(brand, model, year, payload_capacity)
        truck_info = truck.display_info()
        print(
            f"Brand: {truck_info[0]}, Model: {truck_info[1]}, Year: {truck_info[2]}, Payload Capacity: {truck_info[3]}"
        )
