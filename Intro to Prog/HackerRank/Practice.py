def print_rangoli(size):

    alphabet = [chr(97 + i) for i in range(size)]

    rows = []
    for i in range(size):

        char = alphabet[size - 1:i:-1] + alphabet[i:size]

        row = '-'.join(char)
        
        rows.append(row.center(4 * size - 3, '-'))


    full_rangoli = '\n'.join(rows + rows[-2::-1])

    return full_rangoli

    


if __name__ == "__main__":
    n = int(input())
    print(print_rangoli(n))
