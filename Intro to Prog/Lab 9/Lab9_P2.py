import time

def initialize_chunks(n: list) -> list:
    """
    Splits the input list into single-element chunks (lists).
    
    Args:
    n (list): The input list of integers to be chunked.
    
    Returns:
    list: A list of single-element lists.
    """
    # Create chunks of single-element lists
    chunks = [[i] for i in n]
    
    # Print the chunks for debugging purposes
    print(chunks)
    
    # Return the list of chunks
    return chunks


def merge_two_lists(list1: list, list2: list) -> list:
    """
    Merges two sorted lists into one sorted list.
    
    Args:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.
    
    Returns:
    list: The merged sorted list containing elements from both list1 and list2.
    """
    # Initialize pointers for both lists
    merged_list = []
    i = j = 0

    # Compare elements of both lists and append the smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from both lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    # Return the merged sorted list
    return merged_list


def merge_sort(n: list) -> list:
    """
    Perform merge sort on the given list of integers.
    
    Args:
    n (list): The list of integers to be sorted.
    
    Returns:
    list: The sorted list of integers.
    """
    # Initialize the chunks (single-element lists)
    initialized_chunks = initialize_chunks(n)

    # List to store all the merge lists at each step of the sorting process
    all_merge_lists = []

    # Repeat the merging process until we have only one list
    while len(initialized_chunks) > 1:
        # Merge pairs of adjacent chunks
        merged_chunks = [
            (
                merge_two_lists(initialized_chunks[i], initialized_chunks[i + 1])
                if i + 1 < len(initialized_chunks)
                else initialized_chunks[i]
            )
            for i in range(0, len(initialized_chunks), 2)
        ]
        
        # Store the merged chunks at this step for debugging
        all_merge_lists.append(merged_chunks)

        # Update initialized_chunks to the newly merged chunks
        initialized_chunks = merged_chunks

    # Print the final merged list at the first step for debugging
    print(all_merge_lists[0])

    # Return the final sorted list (last chunk in the merged list)
    return initialized_chunks[0]


# Input: A list of integers provided by the user
n = list(map(int, input().strip().split()))

# Record the start time to measure the time taken by the sorting process
start_time = time.perf_counter()

# Perform merge sort on the input list and print the sorted list
print(merge_sort(n))

# Record the end time to measure the time taken by the sorting process
end_time = time.perf_counter()

print(end_time - start_time)
"""
Input: 34 -2 48 7 23 -11 5
Execution time: 0.00012716700439341366 seconds

Input: 34 8 1 2 3 0 9 -2 -100 -99 #3 more values
Execution time: 0.00010987500718329102
"""
