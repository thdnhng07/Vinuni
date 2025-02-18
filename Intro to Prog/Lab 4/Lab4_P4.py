a = input()
b = input()

def division_test(a, b):



    """
    Perform division of two numbers provided as strings.

    Parameters:
    a (str): The numerator as a string.
    b (str): The denominator as a string.

    This function attempts to convert the input strings to floats and performs
    the division. It handles the following exceptions:
    - ValueError: Raised if the inputs cannot be converted to floats.
    - ZeroDivisionError: Raised if the denominator is zero.

    If the division is successful, the result is printed. Regardless of the
    outcome, a message indicating the completion of execution is printed at the end.
    """
    try:
        result = float(a) / float(b)

    except ValueError:
        print('Error: Invalid input.')
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')
    else:
        print('Result: ', result)
    finally:
        print('Execution conplete.')


division_test(a, b)