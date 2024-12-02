import time

def print_pattern_sequential(n):
    """
    Prints a pattern of '*' where each row contains an increasing number of '*' from 1 to n.
    The pattern is printed sequentially in a loop.
    
    Parameters:
        n (int): The number of rows in the pattern.
    """
    # Loop through each row and print '*' repeated row times
    for i in range(n):
        print('*' * (i + 1))


def print_pattern_recurive(n, row=1):
    """
    Prints a pattern of '*' using recursion, where each row contains an increasing number of '*' 
    starting from 1 up to n.
    
    Parameters:
        n (int): The total number of rows in the pattern.
        row (int): The current row being printed, starts from 1. Default is 1.
    """
    # Base case: Stop recursion when row exceeds n
    if row <= n:
        # Print row number of '*' characters
        print('*' * row)
        # Recursively call the function for the next row
        print_pattern_recurive(n, row + 1)


# Read input for the number of rows to print
n = int(input("Enter the number of rows: "))

# Measure and print execution time for the sequential approach
print('Sequential:')
start_time = time.perf_counter()
print_pattern_sequential(n)  # Call function to print pattern sequentially
end_time = time.perf_counter()
print(f"Execution time (Sequential): {end_time - start_time}")

# Measure and print execution time for the recursive approach
print('Recursive:')
start_time = time.perf_counter()

print_pattern_recurive(n)  # Call function to print pattern recursively
end_time = time.perf_counter()
print(f"Execution time (Recursive): {end_time - start_time}")

"""
Sample input and output:

Input: 5
Sequential: 
*
**
***
****
*****
Execution time: 5.266699008643627e-05
Recursive: 
*
**
***
****
*****
Execution time: 1.795799471437931e-05

Input: 10
Sequential: 
*
**
***
****
*****
******
*******
********
*********
**********
Execution time: 0.00017704200581647456
Recursive: 
*
**
***
****
*****
******
*******
********
*********
**********
Execution time: 7.44589779060334e-05
"""
