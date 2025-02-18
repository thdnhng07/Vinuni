class Fraction:
    """
    A class to represent a fraction with a numerator and a denominator. 
    Includes methods for addition, multiplication, simplification, and display.
    """

    def __init__(self, numerator, denominator):
        """
        Initializes a Fraction object.

        Args:
            numerator (int): The numerator part of the fraction.
            denominator (int): The denominator part of the fraction.
        """
        self.__numerator = numerator
        self.__denominator = denominator

    def display(self):
        """
        Prints the fraction in the format 'numerator/denominator'.
        """
        print(f"{self.__numerator}/{self.__denominator}")

    def add(self, other):
        """
        Adds the current fraction with another fraction.

        Args:
            other (Fraction): The other fraction to add.

        Returns:
            Fraction: A new Fraction object representing the sum.
        """
        # Cross-multiply and add to compute the new numerator
        new_numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        # Multiply denominators to compute the new denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        """
        Multiplies the current fraction with another fraction.

        Args:
            other (Fraction): The other fraction to multiply.

        Returns:
            Fraction: A new Fraction object representing the product.
        """
        # Multiply numerators and denominators
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def gcd(a, b):
        """
        Computes the greatest common divisor (GCD) of two integers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The greatest common divisor of a and b.
        """
        while b:  # Use the Euclidean algorithm to compute the GCD
            a, b = b, a % b
        return a

    def simplify(self):
        """
        Simplifies the fraction by dividing the numerator and denominator 
        by their greatest common divisor (GCD).

        Returns:
            Fraction: A new Fraction object in its simplified form.
        """
        gcd_value = Fraction.gcd(self.__numerator, self.__denominator)
        # Divide numerator and denominator by the GCD to simplify
        return Fraction(self.__numerator // gcd_value, self.__denominator // gcd_value)
    
    def numerator(self):
        """
        Returns the numerator of the fraction.
        """
        return self.__numerator
    
    def denominator(self):
        """
        Returns the denominator of the fraction.
        """
        return self.__denominator
# Input handling for two fractions
numerator1, denominator1 = map(int, input().split())  # Input for first fraction
numerator2, denominator2 = map(int, input().split())  # Input for second fraction

# Create Fraction objects
fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

# Compute the sum of the fractions and simplify
sum_fraction = fraction1.add(fraction2).simplify()

# Compute the product of the fractions and simplify
product_fraction = fraction1.multiply(fraction2).simplify()

# Display the results
print(f"{sum_fraction.numerator()}/{sum_fraction.denominator()}")  # Simplified sum
print(f"{product_fraction.numerator()}/{product_fraction.denominator()}")  # Simplified product