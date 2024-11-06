# Take an integer input representing a year
inp = int(input())

# Define a function to check if a year is a leap year
def leap(x):
    # Check if the year is divisible by 4 and not divisible by 100,
    # or if the year is divisible by 400
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return True  # If it satisfies the leap year conditions, return True
    else:
        return False  # Otherwise, return False

# Call the leap function with the input year and print the result
print(leap(inp))
