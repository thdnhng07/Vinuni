import math

a = int ( input () )
b = int ( input () )
c = int ( input () )

# Function to solve quadratic equation a*x^2 + b*x + c = 0
def solve_quadratic (a , b , c ) :

    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
    a (float): Coefficient of the quadratic term.
    b (float): Coefficient of the linear term.
    c (float): Constant term.

    This function calculates the roots of the quadratic equation using the 
    quadratic formula. It handles the following cases:
    - If the equation is linear (a = 0), it calculates the solution using 
      the formula for linear equations.
    - If the discriminant (b^2 - 4ac) is negative, it indicates that there 
      are no real solutions.

    In the case of valid solutions, the function prints the calculated roots.
    """
    try:
        discriminant = b**2 - 4 * a * c
        root1 = (- b + math.sqrt(discriminant)) / (2 * a)
        root2 = (- b - math.sqrt(discriminant)) / (2 * a)
    except ZeroDivisionError:
        print(f"Linear equation, solution: {-c / b}")
    except ValueError:
        print("Attempted to solve the equation.")
        print("Error: No real solutions")
    else:
        print("Attempted to solve the equation.")
        print(f'Solutions: {root1}, {root2}')

solve_quadratic (a , b , c )

