class Polynomial:
    """
    Represents a polynomial using a list of coefficients.
    
    Attributes:
        coefficients (list of int): Coefficients of the polynomial, stored in ascending order of powers.
                                   For example, [1, 2, 3] represents 1 + 2x + 3x^2.
    """

    def __init__(self, coefficients):
        """
        Initializes the Polynomial object with a list of coefficients.

        Args:
            coefficients (list of int): Coefficients of the polynomial.
        """
        self.coefficients = coefficients

    def __add__(self, other):
        """
        Adds two Polynomial objects using the + operator.

        Args:
            other (Polynomial): The other polynomial to add.

        Returns:
            Polynomial: A new Polynomial object representing the sum.
        """
        # Determine the maximum length of the two coefficient lists
        max_len = max(len(self.coefficients), len(other.coefficients))

        # Pad the shorter list with zeros to align the coefficients
        coeff1 = self.coefficients + [0] * (max_len - len(self.coefficients))
        coeff2 = other.coefficients + [0] * (max_len - len(other.coefficients))

        # Compute the sum of coefficients element-wise
        result = [coeff1[i] + coeff2[i] for i in range(max_len)]

        return Polynomial(result)
    
    def __mul__(self, other):
        """
        Multiplies two Polynomial objects using the * operator.

        Args:
            other (Polynomial): The other polynomial to multiply.

        Returns:
            Polynomial: A new Polynomial object representing the product.
        """
        # Initialize the result list with zeros, large enough to store all terms of the product
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        # Perform polynomial multiplication
        for i, c1 in enumerate(self.coefficients):
            for j, c2 in enumerate(other.coefficients):
                result[i + j] += c1 * c2

        return Polynomial(result)
    
    def degree(self):
        """
        Returns the degree of the polynomial.

        Returns:
            int: The degree (highest power with a non-zero coefficient).
        """
        return len(self.coefficients) - 1

    def __str__(self):
        """
        Converts the polynomial to a human-readable string in standard mathematical notation.

        Returns:
            str: The polynomial as a string.
        """
        terms = []  # List to store terms of the polynomial

        for power, coeff in enumerate(self.coefficients):
            if coeff != 0:  # Ignore terms with zero coefficients
                if power == 0:
                    terms.append(f"{coeff}")  # Constant term
                elif power == 1:
                    if coeff == 1:
                        terms.append(f"x")
                    elif coeff == -1:
                        terms.append(f"-x")
                    else:
                        terms.append(f"{coeff}x")
                elif power > 1:
                    if coeff == 1:
                        terms.append(f"x^{power}")
                    elif coeff == -1:
                        terms.append(f"-x^{power}")
                    else:
                        terms.append(f"{coeff}x^{power}")

        # Join terms with ' + ', replacing '+ -' with '- '
        return " + ".join(terms).replace("+ -", "- ").replace('-', '- ') if terms else "0"


# Input polynomials as lists of coefficients
# Representing a + bx + cx^2
poly1 = Polynomial(list(map(int, input().split())))
poly2 = Polynomial(list(map(int, input().split())))

# Compute and print the sum of the two polynomials
sum_poly = poly1 + poly2
print(f"Sum: {sum_poly}")

# Compute and print the product of the two polynomials
product_poly = poly1 * poly2
print(f"Product: {product_poly}")
