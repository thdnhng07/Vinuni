# Taking input for the number of words
n = int(input())

# Dictionary to store lists of anagrams, where the key is the sorted word
anagrams = {}

# Loop over each word input by the user
for i in range(n):
    # Read the word and strip any extra spaces
    word = input().strip()

    # Sort the word alphabetically to normalize its form
    sorted_word = ''.join(sorted(word))

    # If the sorted word is already a key in the dictionary, add the word to the list
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
    else:
        # If the sorted word is not a key, create a new list with the current word
        anagrams[sorted_word] = [word]

# Output the number of unique groups of anagrams
# Each group is represented by the values of the dictionary
print(len(list(anagrams.values())))
