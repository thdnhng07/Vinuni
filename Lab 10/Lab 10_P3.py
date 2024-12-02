def sum_of_digits(num, position=0):
    """
    Recursively calculates the sum of digits in even positions (0-based index) from right to left in a given integer.
    
    Parameters:
        num (int): The integer whose digits will be summed.
        position (int): The current position being processed (default is 0, the rightmost digit).
        
    Returns:
        int: The sum of digits that appear in even positions (0-based index, from right to left).
    """
    # Take the absolute value of the number to handle negative inputs
    num = abs(num)
    
    # Base case: if the number is reduced to 0, return 0
    if num == 0:
        return 0
    
    # Extract the last digit of the number
    last_digit = num % 10
    
    # If the current position is even, add the last digit to the sum
    if position % 2 == 0:
        return last_digit + sum_of_digits(num // 10, position + 1)
    else:
        # Otherwise, continue the recursion without adding the last digit
        return sum_of_digits(num // 10, position + 1)


# Input: Take an integer from the user
num = int(input("Enter a number: "))

# Output: Print the sum of digits in even positions
print(sum_of_digits(num))
