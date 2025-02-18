# Take three integer inputs, separated by spaces, and map them to variables a, b, and c
a, b, c = map(int, input().split())

# Define a function that sorts three numbers and prints them in ascending order
def sort(a, b, c):
    # If a is the smallest, followed by b, and then c
    if a <= b and b <= c:
        print(a, b, c)
    # If a is the smallest, followed by c, and then b
    elif a <= c and c <= b:
        print(a, c, b)
    # If b is the smallest, followed by a, and then c
    elif b <= a and a <= c:
        print(b, a, c)
    # If b is the smallest, followed by c, and then a
    elif b <= c and c <= a:
        print(b, c, a)
    # If c is the smallest, followed by a, and then b
    elif c <= a and a <= b:
        print(c, a, b)
    # If c is the smallest, followed by b, and then a
    else:
        print(c, b, a)

# Call the sort function to sort and print the numbers in ascending order
sort(a, b, c)
