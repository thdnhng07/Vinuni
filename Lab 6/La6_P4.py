def filter_by_length(words, min_length):
    """
    Filters words based on a minimum length requirement.

    Args:
        words (iterable): An iterable containing words (as strings or lists of characters).
        min_length (int): The minimum length a word must have to be included in the output.

    Returns:
        None: The function prints the filtered words, separated by spaces.
    """
    arr = []  # Initialize an empty list to hold the filtered words

    # Iterate over each word in the input iterable
    for word in words:
        # Check if the length of the word meets the minimum length requirement
        if len(word) >= min_length:
            # Join the characters of the word (if it's a list) and append to the results
            arr.append(''.join(word))

    # Print the filtered words, unpacking the list to separate them by spaces
    print(*arr)


# Input handling
n = int(input("Enter the number of words: "))  # Read the number of words
words = map(list, input("Enter the words separated by spaces: ").split())  # Read and split the input into lists of characters
min_length = int(input("Enter the minimum length: "))  # Read the minimum length requirement

# Call the filtering function
filter_by_length(words, min_length)
