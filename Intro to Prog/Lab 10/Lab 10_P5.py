def permutations_generator(n):
    """
    Generates all possible permutations of a list of distinct integers using recursion.

    Parameters:
        n (list): A list of distinct integers for which permutations need to be generated.

    Returns:
        list: A list of lists, where each inner list is a permutation of the input list.
    """
    # Base case: if the list has one or fewer elements, return it as the only permutation
    if len(n) <= 1:
        return [n]
    
    permutations = []

    # Iterate through each element in the list
    for i in range(len(n)):
        # Create the 'rest' list by excluding the element at index i
        rest = n[:i] + n[i+1:]
        
        # Recursively generate permutations of the 'rest' of the list
        for perm in permutations_generator(rest):
            # Prepend the current element (n[i]) to each of the permutations of the 'rest'
            permutations.append([n[i]] + perm)

    return permutations


# Input: Read a list of integers from the user
n = list(map(int, input().split()))

# Generate all permutations of the input list
result = permutations_generator(n)

# Sort and print each permutation
for perm in sorted(result):
    print(*perm)
