def smallest_integer_for(prompt):
    """
    Finds the smallest positive integer not present in the input sequence using a for loop.

    Parameters:
    prompt (iterable): An iterable (such as a list) containing integers.

    Returns:
    int: The smallest positive integer that is missing from the input sequence.
    """
    # Remove duplicates and sort the input numbers
    number = sorted(set(prompt))

    # Check each integer starting from 1 up to the length of `number` + 1
    # The first missing positive integer is returned
    for i in range(1, len(number) + 2):
        if i not in number:
            return i


def smallest_integer_while(prompt):
    """
    Finds the smallest positive integer not present in the input sequence using a while loop.

    Parameters:
    prompt (iterable): An iterable (such as a list) containing integers.

    Returns:
    int: The smallest positive integer that is missing from the input sequence.
    """
    # Remove duplicates and sort the input numbers
    number = sorted(set(prompt))

    # Initialize missing_number as 1, the smallest positive integer
    missing_number = 1

    # Increment missing_number until it is no longer found in `number`
    while missing_number in number:
        missing_number += 1
    return missing_number


# Prompt user for input, converts each entry to an integer
prompt = map(int, input("Enter a sequence of integers separated by spaces: ").split())

# Output the results of both functions
print("Smallest missing integer (for loop):", smallest_integer_for(prompt))
print("Smallest missing integer (while loop):", smallest_integer_while(prompt))
