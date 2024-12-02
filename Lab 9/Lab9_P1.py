import time

def find_min_max(arr: list) -> int:
    """
    Find the minimum and maximum values in the array.

    Args:
    arr (list): List of integers.

    Returns:
    tuple: (min_value, max_value)
    """
    max_value = max(arr)
    min_value = min(arr)
    return min_value, max_value


def count_frequency(arr: list) -> list:
    """
    Count the frequency of each number in the range [min_value, max_value].

    Args:
    arr (list): List of integers.

    Returns:
    list: List of frequencies corresponding to the range.
    """
    min_value, max_value = find_min_max(arr)
    frequency = {}

    for num in range(min_value, max_value + 1):
        frequency[num] = arr.count(num)

    frequency_value = [value for value in frequency.values()]

    return frequency_value


def counting_sort(arr: list) -> list:
    """
    Sort the array using counting sort algorithm.

    Args:
    arr (list): List of integers.

    Returns:
    list: Sorted list.
    """
    min_value, max_value = find_min_max(arr)
    frequency = count_frequency(arr)
    sorted_arr = []

    for i, count in enumerate(frequency):
        sorted_arr.extend([i + min_value] * count)

    return sorted_arr


# Input and Function Calls
arr = list(map(int, input().split()))
start_time = time.perf_counter()
# Finding min and max values
print(*find_min_max(arr))

# Counting frequency
print(count_frequency(arr))

# Sorting the array
print(counting_sort(arr))

end_time = time.perf_counter()

print(end_time - start_time)
"""
Input: 8 3 1 7 0 0 4 2
Execution time: 0.0002185420016758144 seconds

Input: 10 9 8 7 6 5 4 3 2 -1 #2 more values
Execution time: 0.00028504099464043975 seconds
"""
