class Car:
    """
    A class representing a car with attributes for speed, fuel consumption rate, and fuel level.
    Includes methods to check if the car can reach a destination and calculate refueling costs.
    """

    def __init__(self, speed, consumption_rate, fuel_level):
        """
        Initializes a Car object with speed, fuel consumption rate, and current fuel level.

        Args:
            speed (int): The speed of the car (km/h).
            consumption_rate (int): The fuel consumption rate of the car (units per hour).
            fuel_level (int): The current fuel level of the car (in units).
        """
        self.speed = speed
        self.consumption_rate = consumption_rate
        self.fuel_level = fuel_level

    def can_reach(self, distance):
        """
        Determines whether the car can reach a given distance with the current fuel level.

        Args:
            distance (int): The distance the car needs to travel (in kilometers).

        Returns:
            bool: True if the car can reach the destination, False otherwise.
        """
        # Calculate the required travel time and fuel usage, and check if fuel is sufficient.
        return distance // self.speed <= self.fuel_level // self.consumption_rate

    def refuel_cost(self, price_per_unit):
        """
        Calculates the cost to refuel the car to a full tank (100 units).

        Args:
            price_per_unit (float): The price per unit of fuel.

        Returns:
            float: The cost to refill the car's tank to 100 units.
        """
        # Calculate the fuel required to reach a full tank and multiply by the price per unit.
        return (100 - self.fuel_level) * price_per_unit


# Input: speed, fuel consumption rate, fuel level, distance, and price per unit of fuel.
speed, consumption_rate, fuel_level, distance, price_per_unit = map(
    lambda x: float(x) if '.' in x else int(x), input().split()
)

# Create a Car object with the provided input.
car = Car(speed, consumption_rate, fuel_level)

# Output the car's attributes.
print(car.speed, car.consumption_rate, car.fuel_level)

# Output whether the car can reach the destination.
print(car.can_reach(distance))

# Output the cost to refuel the car to full capacity.
print(car.refuel_cost(price_per_unit))
