def median(num, arr):
    """
    Calculates the median of a list of numbers.

    The median is the middle value in a sorted list. If the number of elements is odd, the median is the middle element.
    If the number of elements is even, the median is the average of the two middle elements.

    Parameters:
    num (int): The number of elements in the array (not used directly, but can be used for validation).
    arr (list of int): A list of integers for which the median will be calculated.

    Returns:
    float: The median of the list. If the list has an even number of elements, the result will be a float (average of two middle values).
           If the list has an odd number of elements, the result will be an integer (the middle element).
    """
    # Sort the array in ascending order to find the median
    arr.sort()
    
    # Get the number of elements in the array
    n = len(arr)
    
    # Calculate the middle index
    mid = n // 2

    # Check if the number of elements is even
    if n % 2 == 0:
        # Return the average of the two middle elements if even
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        # Return the middle element if odd
        return arr[mid]

# Read the input: number of elements and the list of integers
number = int(input())
arr = list(map(int, input().split()))

# Print the median, formatted to 1 decimal place
print(f'{median(number, arr):.1f}')
