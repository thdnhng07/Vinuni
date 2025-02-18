def sorting(string: str, custom_order: str) -> str:
    """
    Sorts the characters of a string according to a specified custom alphabet order.

    Parameters:
    string (str): The string that needs to be sorted.
    custom_order (str): A string representing the custom alphabet order.

    Returns:
    str: The string rearranged according to the custom order.
    """
    
    # Step 1: Create a dictionary mapping each character in custom_order to its index.
    # This helps in defining the "priority" of each character according to custom_order.
    char_order = {char: index for index, char in enumerate(custom_order)}
    
    # Step 2: Sort the string based on the custom order.
    # The 'key' for sorting is defined by the char_order dictionary which tells Python
    # to use the index of each character in the custom order for sorting.
    sorted_string = "".join(sorted(string, key=lambda char: char_order[char]))

    # Step 3: Print and return the sorted string.
    print(sorted_string)
    return sorted_string


# Example usage:
str_input = input()
custom_order = input()

# Call the function with example inputs
sorting(str_input, custom_order)
