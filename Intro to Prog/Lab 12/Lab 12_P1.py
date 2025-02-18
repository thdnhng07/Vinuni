class Employee:
    """
    Base class for representing an employee.
    
    Attributes:
        __name (str): The name of the employee (private).
        __employee_id (str): The unique identifier for the employee (private).
    """
    def __init__(self, name, employee_id):
        """
        Initializes the Employee with a name and employee ID.
        
        Args:
            name (str): The name of the employee.
            employee_id (str): The unique ID for the employee.
        """
        self.__name = name
        self.__employee_id = employee_id

    def calculate_salary(self):
        """
        Placeholder method to calculate the salary of the employee.
        Must be implemented by subclasses.
        
        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError


class FullTimeEmployee(Employee):
    """
    Represents a full-time employee.
    
    Attributes:
        monthly_salary (float): The monthly salary of the employee.
    """
    def __init__(self, name, employee_id, monthly_salary):
        """
        Initializes a FullTimeEmployee instance.
        
        Args:
            name (str): The name of the employee.
            employee_id (str): The unique ID for the employee.
            monthly_salary (float): The fixed monthly salary of the employee.
        """
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        """
        Calculates the monthly salary of the full-time employee.
        
        Returns:
            float: The monthly salary.
        """
        return self.monthly_salary

    def __str__(self):
        """
        Returns a string representation of the full-time employee, including their
        employee ID, name, and salary.
        
        Returns:
            str: Formatted string with employee details and salary.
        """
        return f"Employee ID: {self._Employee__employee_id}, Name: {self._Employee__name}, Salary: {self.calculate_salary():.1f}"


class PartTimeEmployee(Employee):
    """
    Represents a part-time employee.
    
    Attributes:
        hourly_rate (float): The hourly pay rate for the employee.
        hours_worked (int): The total number of hours worked by the employee.
    """
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        """
        Initializes a PartTimeEmployee instance.
        
        Args:
            name (str): The name of the employee.
            employee_id (str): The unique ID for the employee.
            hourly_rate (float): The pay rate per hour.
            hours_worked (int): The total hours worked.
        """
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """
        Calculates the total salary based on the hourly rate and hours worked.
        
        Returns:
            float: The calculated salary.
        """
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        """
        Returns a string representation of the part-time employee, including their
        employee ID, name, and calculated salary.
        
        Returns:
            str: Formatted string with employee details and salary.
        """
        return f"Employee ID: {self._Employee__employee_id}, Name: {self._Employee__name}, Salary: {self.calculate_salary():.1f}"


# Input processing
for _ in range(int(input())):
    data = input().split()
    
    # Determine the type of employee and create the appropriate instance
    if len(data) == 3:  # Full-time employee
        employee_id, name, monthly_salary = data
        full_time = FullTimeEmployee(name, employee_id, int(monthly_salary))
        print(full_time)

    elif len(data) == 4:  # Part-time employee
        employee_id, name, hourly_rate, hours_worked = data
        part_time = PartTimeEmployee(name, employee_id, int(hourly_rate), int(hours_worked))
        print(part_time)
