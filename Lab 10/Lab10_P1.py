import time

def fibonacci_sequential(n):
    """
    Calculates the nth Fibonacci number using an iterative (sequential) approach.
    
    Parameters:
        n (int): The index of the Fibonacci number to calculate (n >= 0).
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    
    # Initialize the Fibonacci sequence for the first two numbers
    fibonacci_sequence = [0, 1]

    # Calculate Fibonacci numbers iteratively
    for i in range(2, n + 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    return fibonacci_sequence[-1]


def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using a recursive approach.
    
    Parameters:
        n (int): The index of the Fibonacci number to calculate (n >= 0).
        
    Returns:
        int: The nth Fibonacci number.
    """
    # Base cases for recursion
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        # Recursive call for Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Take user input for the Fibonacci index to calculate
n = int(input("Enter the Fibonacci index: "))

# Measure and print execution time for the sequential approach
start_time = time.perf_counter()
print(f'Sequential: {fibonacci_sequential(n)}')
end_time = time.perf_counter()
print(f"Execution time (Sequential): {end_time - start_time}")

# Measure and print execution time for the recursive approach
start_time = time.perf_counter()
print(f'Recursive: {fibonacci_recursive(n)}')
end_time = time.perf_counter()
print(f"Execution time (Recursive): {end_time - start_time}")

"""
Sample input and output:

Input: 10
Sequential: 55
Execution time: 0.00011916700168512762
Recursive: 55
Execution time: 4.033301956951618e-05

Input: 20
Sequential: 6765
Execution time: 0.00010829200618900359
Recursive: 6765
Execution time: 0.002974165981868282
"""
