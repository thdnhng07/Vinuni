# Convert input to lower case
inp = input()
inp = inp.lower()


# Define a function

def count_vowels(text):

    vowels = 'aieou'
    counter = 0

# Iterate over each character in the input text and check if it's a vowel
    for char in text:
        if char in vowels:
            counter += 1


    return counter

print(count_vowels(inp))