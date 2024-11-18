def find_max_distinct():
    """
    Finds the maximum number of distinct elements in any subarray of a specified size
    from an input array.

    The function reads:
    1. The size of the array.
    2. The elements of the array.
    3. The size of the subarray to consider.

    It then computes and prints the maximum number of distinct elements in any
    contiguous subarray of the given size.
    """

    # Read the size of the array
    arr_size = int(input())

    # Read the array elements
    arr = list(map(int, input().split()))

    # Read the size of the subarray
    subarr_size = int(input())

    # Initialize the variable to store the maximum number of distinct elements in a subarray
    max_distinct_sub_arr = 0

    # Loop through each possible subarray of the specified size
    for i in range(arr_size - subarr_size + 1):

        # Get the current subarray slice
        sub_arr = arr[i:i + subarr_size]

        # Count distinct elements in the current subarray
        distinct_elements = len(set(sub_arr))

        # Update max distinct count if the current subarray has more distinct elements
        if distinct_elements > max_distinct_sub_arr:
            max_distinct_sub_arr = distinct_elements

    # Print the maximum number of distinct elements found
    print(max_distinct_sub_arr)

# Execute the function
find_max_distinct()
