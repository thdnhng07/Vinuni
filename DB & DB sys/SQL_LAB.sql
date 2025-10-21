USE qacs;
# A. Using the SALE table in qacs database:
# 1. Can you find a function to extract the day of the year from SaleDate (which run from 1-366)? 
SELECT SaleID, SaleDate, dayofyear(SaleDate) AS DayOfYear
FROM SALE;

# 2. Given the SaleDate, can you compute how many days until the end of the corresponding month for each SaleDate?
SELECT SaleDate, SaleID, datediff(LAST_DAY(SaleDate), SaleDate) As DayTillEnd
FROM SALE;

# 3. Extract the 1st day of the month for the corresponding month of each SaleDate?
SELECT SaleDate, SaleID, date_format(SaleDate, '%Y-%m-01') AS FirstOfMonth
FROM SALE;

# B. How many items from each vendor is available in the store?
SELECT VendorID,COUNT(*) AS TotalItemsAvailable
FROM Item
group by VendorID;

# C. How many items from each vendor is available in the store? Sort by the number of items from highest to lowest. 
SELECT VendorID,COUNT(*) AS TotalItemsAvailable
FROM Item
group by VendorID
order by TotalItemsAvailable desc;

# D. Find the customers with a single purchase at the store.
SELECT CustomerID
FROM SALE
GROUP BY CustomerID
HAVING COUNT(*) = 1;

# E. Find all the phone number and email address of customers with a single purchase at the store.
SELECT c.CustomerID, c.FirstName, c.LastName, c.Phone, c.EmailAddress
FROM CUSTOMER c
WHERE c.CustomerID IN (
  SELECT CustomerID
  FROM SALE
  GROUP BY CustomerID
  HAVING COUNT(*) = 1
);

# F. Find the number of sales of each sale date. 
SELECT DATE(SaleDate) AS SaleDay, COUNT(*) AS NumSales
FROM SALE
GROUP BY DATE(SaleDate)
ORDER BY SaleDay;

# G. Retrieve the first name and last name of the best performing employee in 2019 according to total sale value. (Do NOT use JOIN here)
SELECT FirstName, LastName
FROM Employee
WHERE EmployeeID = (
    SELECT EmployeeID
    FROM Sale
    WHERE YEAR(SaleDate) = 2019
    GROUP BY EmployeeID
    ORDER BY SUM(Total) DESC
    LIMIT 1
);
