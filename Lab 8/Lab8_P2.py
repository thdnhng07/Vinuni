def work_hours():
    """
    Reads the employee work data, calculates the total weekly hours for each employee,
    filters employees who worked more than 40 hours, sorts them in descending order by 
    total hours (and by name in ascending order if hours are equal), and prints the result.

    Input:
    - First line: integer n (number of employees)
    - Next n lines: each containing the name of the employee followed by 7 integers 
      representing hours worked each day of the week.
    
    Output:
    - A sorted list of tuples with the name of each employee and their total hours, 
      in descending order of hours for those who worked more than 40 hours. 
      Returns an empty list if no employee worked over 40 hours.
    """
    
    # Read the number of employees
    n = int(input())
    
    # Initialize lists to store employee data and weekly total hours
    employees = []
    sum_hours = []
    
    # Loop through each employee's data
    for i in range(n):
        data = input().split()  # Split input into name and hours worked each day
        name = data[0]
        hours = list(map(int, data[1:]))  # Convert hours to integers and store in a list
        employees.append((name, hours))  # Store employee's name and hours in a tuple
        
        total_hours = sum(hours)  # Calculate total hours worked for the week
        
        # Append tuple with employee's name and total hours worked to sum_hours
        sum_hours.append((name, total_hours))
    
    # Filter employees who worked more than 40 hours
    over_40_hours = [(name, total_hours) for name, total_hours in sum_hours if total_hours > 40]
    
    # Sort employees based on total hours (descending) and name (ascending)
    over_40_hours.sort(key=lambda x: (-x[1], x[0]))
    
    # Output the result
    print(over_40_hours)


# Run the function to execute
work_hours()






