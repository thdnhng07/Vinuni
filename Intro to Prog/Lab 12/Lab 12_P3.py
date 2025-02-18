class Vehicle:
    """
    Base class for vehicles.

    Attributes:
        brand (str): Brand of the vehicle
        model (str): Model of the vehicle
        year (int): Year of manufacture
    """

    def __init__(self, brand, model, year):
        """
        Initialize a Vehicle object.

        Args:
            brand (str): Brand of the vehicle
            model (str): Model of the vehicle
            year (int): Year of manufacture
        """
        self.brand = brand
        self.model = model
        self.year = int(year)

    def display_info(self):
        """
        Return information about the vehicle.

        Returns:
            tuple: Brand, model, and year of the vehicle
        """
        return self.brand, self.model, self.year


class Car(Vehicle):
    """
    Subclass for cars, inheriting from Vehicle.
    
    Attributes:
        num_doors (int): Number of doors in the car
    """

    def __init__(self, brand, model, year, num_doors):
        """
        Initialize a Car object.

        Args:
            brand (str): Brand of the car
            model (str): Model of the car
            year (int): Year of manufacture
            num_doors (int): Number of doors in the car
        """
        super().__init__(brand, model, year)
        self.num_doors = int(num_doors)

    def display_info(self):
        """
        Return information about the car, including number of doors.

        Returns:
            tuple: Brand, model, year, and number of doors of the car
        """
        return (*super().display_info(), self.num_doors)


class Truck(Vehicle):
    """
    Subclass for trucks, inheriting from Vehicle.
    
    Attributes:
        payload_capacity (float): Payload capacity of the truck
    """

    def __init__(self, brand, model, year, payload_capacity):
        """
        Initialize a Truck object.

        Args:
            brand (str): Brand of the truck
            model (str): Model of the truck
            year (int): Year of manufacture
            payload_capacity (float): Payload capacity of the truck
        """
        super().__init__(brand, model, year)
        self.payload_capacity = float(payload_capacity)

    def display_info(self):
        """
        Return information about the truck, including payload capacity.

        Returns:
            tuple: Brand, model, year, and payload capacity of the truck
        """
        return (*super().display_info(), self.payload_capacity)


# Main program logic
for _ in range(int(input())):
    data = input().split()
    vehicle_type = data[0]

    if vehicle_type == "Car":
        _, brand, model, year, num_doors = data
        car_info = Car(brand, model, year, num_doors).display_info()
        print(
            f"Brand: {car_info[0]}, Model: {car_info[1]}, Year: {car_info[2]}, Number of doors: {car_info[3]}"
        )
    elif vehicle_type == "Truck":
        _, brand, model, year, payload_capacity = data
        truck_info = Truck(brand, model, year, payload_capacity).display_info()
        print(
            f"Brand: {truck_info[0]}, Model: {truck_info[1]}, Year: {truck_info[2]}, Payload Capacity: {truck_info[3]}"
        )