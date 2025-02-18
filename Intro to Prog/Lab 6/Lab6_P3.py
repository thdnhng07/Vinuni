def enumerate_positive(numbers):
    """
    This function takes a list of integers and returns a list of sublists, where each sublist contains the index and 
    value of the positive numbers from the input list.
    
    Args:
    numbers (list of int): A list of integers to be processed.

    Returns:
    list of lists: A list of sublists where each sublist contains two elements:
                   - the index of a positive number in the input list,
                   - the positive number itself.
    """
    arr = []  # Initialize an empty list to store the results
    for i, element in enumerate(numbers):  # Loop through the list with both index (i) and element
        if element > 0:  # Check if the element is positive
            arr.append([i, element])  # Append the index and the positive number as a sublist to arr
    
    return arr  # Return the list of sublists

# Input handling
n = int(input())  # Read the number of elements in the list
numbers = list(map(int, input().split()))  # Read the list of numbers as integers

# Call the function and print the result
print(enumerate_positive(numbers))
