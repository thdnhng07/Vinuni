def count_word_frequency(text):
    """
    Counts the frequency of each unique word in a given text, prints the number 
    of unique words, and displays the word frequencies in alphabetical order.
    
    Parameters:
    text (str): The input text to analyze.

    Returns:
    None
    """
    
    # Convert the text to lowercase to ensure case insensitivity
    text = text.lower()
    
    # Split the text into individual words
    words = text.split()
    
    # Initialize an empty dictionary to store word frequencies
    word_frequency = {}

    # Count occurrences of each word
    for word in words:
        # Increment word count, defaulting to 0 if the word is not yet in the dictionary
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    # Get the count of unique words
    unique_word_count = len(word_frequency)

    # Format word frequencies as a sorted, comma-separated string
    sorted_word_frequency = ", ".join(f"{word}: {count}" for word, count in sorted(word_frequency.items()))

    # Print the unique word count
    print(unique_word_count)
    
    # Print the sorted word frequency
    print(sorted_word_frequency)


# Get user input and remove any leading/trailing whitespace
text = input("Enter text: ").strip()

# Call the function with the provided text
count_word_frequency(text)
