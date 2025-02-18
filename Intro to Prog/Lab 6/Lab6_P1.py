def list_operations(numbers):
    """
    Perform and print various operations on a list of numbers:
    
    1. Calculate and print the sum of all elements in the list.
    2. Find and print the minimum value in the list.
    3. Find and print the maximum value in the list.
    4. Reverse the list and print the reversed list as space-separated values.
    
    Args:
    numbers (list of int): A list of integers to perform operations on.

    Output:
    Prints the sum, minimum value, maximum value, and the reversed list.
    """

    # 1. Calculate the sum of all elements in the list
    total = sum(numbers)

    # 2. Find the minimum value in the list
    min_value = min(numbers)

    # 3. Find the maximum value in the list
    max_value = max(numbers)

    # 4. Reverse the list
    reversed_list = numbers[::-1]

    # Print the results in the required order
    print(total)        # Print the sum of the list
    print(min_value)    # Print the minimum value
    print(max_value)    # Print the maximum value
    print(*reversed_list)  # Print the reversed list, unpacked to avoid square brackets


# Input handling
n = int(input())  # Read the number of elements
numbers = list(map(int, input().split()))  # Read the list of numbers

# Call the function to perform list operations
list_operations(numbers)
