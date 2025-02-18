def analyze_words(words):
    """
    Analyze character frequencies in a list of words.

    This function takes a list of words and prints the frequency of each unique character 
    in each word, formatted with the word index. The character counts are presented in 
    alphabetical order.

    Parameters:
    words (list of str): A list of words for which character frequencies will be analyzed.

    Output:
    Prints a formatted string for each word in the list, showing the index of the word and 
    the count of each character in the format "index - char1: count1, char2: count2, ...".
    """

    # Iterate over each word along with its index
    for index, word in enumerate(words):
        # Create a dictionary to count occurrences of each character in the word
        character_count = {char: word.count(char) for char in sorted(set(word))}

        # Prepare the output string, sorting character counts alphabetically
        output = f'{index} - ' + ', '.join(f'{char}: {count}' for char, count in sorted(character_count.items()))
        
        # Print the formatted output
        print(output)

# Read the number of words from input
n = int(input("Enter the number of words: "))  # Number of words
# Read the words from input, splitting them into a list
words = input("Enter the words separated by spaces: ").split()  # Corrected to split into words
# Call the function with the list of words
analyze_words(words)
