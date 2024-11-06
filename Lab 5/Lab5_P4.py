# Take an input string from the user
prompt = input()

# Define a function 'decoder' that takes a string and performs various transformations
def decoder(prompt: str) -> str:
    # Check if the word 'secret' is in the string
    if 'secret' in prompt:
        # If 'secret' is found, replace it with 'XXXXXX'
        prompt = prompt.replace('secret', 'XXXXXX')
    
    # Check if the letter 'a' is in the string
    if 'a' in prompt:
        # Replace all occurrences of 'a' with '@'
        prompt = prompt.replace('a', '@')
    
    # Check if the letter 'e' is in the string
    if 'e' in prompt:
        # Replace all occurrences of 'e' with '3'
        prompt = prompt.replace('e', '3')
    
    # Check if the letter 'i' is in the string
    if 'i' in prompt:
        # Remove all occurrences of 'i' by replacing it with an empty string
        prompt = prompt.replace('i', '')
    
    # Check if the letter 'o' is in the string
    if 'o' in prompt:
        # Replace all occurrences of 'o' with '0'
        prompt = prompt.replace('o', '0')
    
    # Check if the letter 'u' is in the string
    if 'u' in prompt:
        # Replace all occurrences of 'u' with 'v'
        prompt = prompt.replace('u', 'v')

    # Check if the length of the modified string is even
    if len(prompt) % 2 == 0:
        # If the length is even, convert the entire string to uppercase
        prompt = prompt.upper()
    else:
        # If the length is odd, convert the entire string to lowercase
        prompt = prompt.lower()

    # Return the modified string
    return prompt

# Call the decoder function with the input string and print the result
print(decoder(prompt))
