def calculate_area(length: int, width: int, ) -> int:

    """
    Calculate the area of a rectangle given its length and width.

    This function takes two positive integers as inputs, representing the
    length and width of a rectangle. It asserts that both values are
    greater than zero before calculating and returning the area.

    Parameters:
        length (int): The length of the rectangle. Must be a positive integer.
        width (int): The width of the rectangle. Must be a positive integer.

    Returns:
        int: The area of the rectangle, calculated as length * width.

    Raises:
        AssertionError: If either length or width is not a positive integer.
    """
    assert length > 0, 'Length must be a psoitive integer'
    assert width > 0, 'Width must be a positive integer'

    return length * width


print('Area: ', calculate_area(int(input()), int(input())))