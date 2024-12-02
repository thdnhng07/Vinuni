def is_special_palindrome(inp_str, diff=0):
    """
    Recursively checks if the input string is a special palindrome. A string is considered
    a special palindrome if the number of differing characters between the string and its reverse
    is less than or equal to 2.

    Parameters:
        inp_str (str): The input string to be checked.
        diff (int): The count of differing characters (default is 0).

    Returns:
        bool: True if the string is a special palindrome, False otherwise.
    """
    # Base case: If the string has 1 or 0 characters, it's considered a palindrome
    if len(inp_str) <= 1:
        return True
    
    # If the first and last characters are different, increment the 'diff' counter
    if inp_str[0] != inp_str[-1]:
        diff += 1

    # If more than 2 differences are found, it's not a special palindrome
    if diff > 2:
        return False
    
    # Recursively check the substring excluding the first and last characters
    return is_special_palindrome(inp_str[1:-1], diff)


# Input string from the user
input_str = input()

# Output whether the input string is a special palindrome
print(is_special_palindrome(input_str))
