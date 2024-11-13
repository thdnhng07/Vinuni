n = int(input())

anagrams = {}

for i in range(n):

    word = input().strip()

    sorted_word = ''.join(sorted(word))

    if sorted_word in anagrams:

        anagrams[sorted_word].append(word)

    else:

        anagrams[sorted_word] = [word]

print(len(list(anagrams.values())))
