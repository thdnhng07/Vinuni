def kth_largest(arr, k):
    """
    Finds the k-th largest element in an unsorted list using binary search.

    Parameters:
        arr (list): The unsorted list of integers.
        k (int): The 1-based index of the k-th largest element.

    Returns:
        int: The k-th largest element in the array.
    """
    # Step 1: Determine the range for binary search (minimum and maximum in the array)
    low, high = min(arr), max(arr)

    # Step 2: Perform binary search
    while low < high:
        mid = (low + high + 1) // 2  # Middle of the current range
        count = sum(1 for num in arr if num >= mid)  # Count elements >= mid

        # Adjust binary search range based on the count
        if count >= k:
            low = mid  # Mid could be the k-th largest, search in the upper half
        else:
            high = mid - 1  # Mid is too large, search in the lower half

    # When the loop ends, low will hold the k-th largest element
    return low

arr = list(map(int, input().split()))
k = int(input())
print(kth_largest(arr, k))
