def star_pyramid(n):
    """
    Prints a pyramid of stars with a given height.

    Args:
        n (int): The number of levels (rows) in the pyramid.
    
    The function generates each level of the pyramid by calculating 
    the necessary spaces and stars, then prints the level line by line.
    """
    for i in range(1, n + 1):
        # Calculate the number of spaces needed for left alignment
        space = ' ' * (n - i)
        
        # Calculate the number of stars for the current row
        star = '*' * (2 * i - 1)
        
        # Print the spaces followed by the stars to form a centered pyramid row
        print(space + star)

# Get user input for the number of levels in the pyramid
n = int(input("Enter the number of rows for the pyramid: "))
star_pyramid(n)
