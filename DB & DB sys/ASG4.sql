-- USE QACS
use qacs;

-- 1. Best-Selling Item by Year: For each year, find the item with the highest total sales revenue

Select * from `Sale_Item`,`Sale`;

SELECT r.Year, r.ItemID, i.ItemDescription, ROUND(r.Revenue,2) AS Revenue
FROM (
  SELECT YEAR(s.SaleDate) AS Year,
         si.ItemID,
         SUM(si.ItemPrice) AS Revenue
  FROM SALE s
  JOIN SALE_ITEM si ON si.SaleID = s.SaleID
  GROUP BY YEAR(s.SaleDate), si.ItemID
) r
JOIN (
  SELECT Year, MAX(Revenue) AS MaxRev
  FROM (
    SELECT YEAR(s.SaleDate) AS Year,
           si.ItemID,
           SUM(si.ItemPrice) AS Revenue
    FROM SALE s
    JOIN SALE_ITEM si ON si.SaleID = s.SaleID
    GROUP BY YEAR(s.SaleDate), si.ItemID
  ) t
  GROUP BY Year
) m
  ON r.Year = m.Year AND r.Revenue = m.MaxRev
JOIN ITEM i ON i.ItemID = r.ItemID
ORDER BY r.Year;

-- 2. Employee Performance (Orders, Revenue, Share, and Difference from Average): For each employee, show the number of orders handled, total sales revenue, the share of total revenue, and the difference from the average employee revenue.
select * from `employee`, `sale`; 

WITH emp AS (
  SELECT
    s.EmployeeID,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    COUNT(DISTINCT s.SaleID) AS OrdersHandled,
    SUM(si.ItemPrice) AS EmployeeRevenue
  FROM SALE s
  JOIN SALE_ITEM si ON si.SaleID = s.SaleID
  JOIN EMPLOYEE e ON e.EmployeeID = s.EmployeeID
  GROUP BY s.EmployeeID, EmployeeName
)
SELECT
  EmployeeID,
  EmployeeName,
  OrdersHandled,
  ROUND(EmployeeRevenue, 2) AS EmployeeRevenue,
  ROUND(EmployeeRevenue / NULLIF(SUM(EmployeeRevenue) OVER (), 0), 6) AS RevenueShare,
  ROUND(EmployeeRevenue - AVG(EmployeeRevenue) OVER (), 2)         AS DiffFromAvgEmp
FROM emp
ORDER BY EmployeeRevenue DESC;

-- 3. Days Since Previous Order per Customer: For each sale, calculate the number of days since the same customer’s previous purchase. Show NULL if it’s their first order
with s as (
	select
		SaleID,
        CustomerID,
        SaleDate,
        lag(SaleDate) over (
			partition by CustomerID
            order by SaleDate, SaleID
	) as PrevsaleDate
	from SALE
)
select
	SaleID,
    CustomerID,
    SaleDate,
    PrevSaleDate,
    case
		when PrevSaleDate is null then null
        else datediff(SaleDate, PrevSaleDate)
	end as DaysSincePrev
From s
order by CustomerID, SaleDate, SaleID;

-- 4. Top-3 Items by Revenue per Customer: For each customer, list their top three items based on total sales revenue.
WITH rev AS (
  SELECT
    s.CustomerID,
    si.ItemID,
    SUM(si.ItemPrice) AS Revenue
  FROM SALE s
  JOIN SALE_ITEM si ON si.SaleID = s.SaleID
  GROUP BY s.CustomerID, si.ItemID
),
ranked AS (
  SELECT
    CustomerID,
    ItemID,
    Revenue,
    ROW_NUMBER() OVER (
      PARTITION BY CustomerID
      ORDER BY Revenue DESC, ItemID
    ) AS rn
  FROM rev
)
SELECT
  r.CustomerID,
  r.ItemID,
  i.ItemDescription,
  ROUND(r.Revenue, 2) AS Revenue
FROM ranked r
JOIN ITEM i ON i.ItemID = r.ItemID
WHERE r.rn <= 3
ORDER BY r.CustomerID, r.Revenue DESC, r.ItemID;

-- 5. Monthly Revenue and 3-Month Moving Average: Display total revenue for each month and the 3-month moving average (current month + 2 previous months).
select * from sale;

WITH monthly AS (
  SELECT
    DATE_FORMAT(s.SaleDate, '%Y-%m-01') AS month_start,
    SUM(si.ItemPrice) AS revenue
  FROM SALE s
  JOIN SALE_ITEM si ON si.SaleID = s.SaleID
  GROUP BY DATE_FORMAT(s.SaleDate, '%Y-%m-01')
)
SELECT
  month_start,
  ROUND(revenue, 2) AS revenue,
  ROUND(
    AVG(revenue) OVER (
      ORDER BY month_start
      ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 6
  ) AS revenue_ma3
FROM monthly
ORDER BY month_start;

-- USE NORTHWIND
use Northwind;

-- 1. Show the product (all columns) whose deviation between List Price and Standard Cost is the largest. 
SELECT p.*
FROM Products AS p
ORDER BY ABS(p.`List Price` - p.`Standard Cost`) DESC
LIMIT 1;

-- 2. Show the best seller product(s) (which is one being ordered the most so far)
WITH totals AS (
  SELECT
    od.`Product ID` AS ProductID,
    SUM(od.`Quantity`) AS TotalQty
  FROM `order details` od
  GROUP BY od.`Product ID`
),
ranked AS (
  SELECT *,
         DENSE_RANK() OVER (ORDER BY TotalQty DESC) AS rk
  FROM totals
)
SELECT
  p.`ID`          AS ProductID,
  p.`Product Name`,
  r.TotalQty
FROM ranked r
JOIN products p ON p.`ID` = r.ProductID
WHERE r.rk = 1
ORDER BY ProductID;

-- 3. Show the list of product names that have not been ordered ever.
SELECT p.`Product Name`
FROM products AS p
WHERE NOT EXISTS (
  SELECT 1
  FROM `order details` AS od
  WHERE od.`Product ID` = p.`ID`
)
ORDER BY p.`Product Name`;

-- 4. Show how many orders each CustomerID has placed.
SELECT
  o.`Customer ID` AS CustomerID,
  COUNT(*)        AS No_Orders
FROM `orders` o
GROUP BY o.`Customer ID`
ORDER BY CustomerID;

-- 5. Identify the employee ID corresponding to the employee having the highest number of orders.
WITH counts AS (
  SELECT o.`Employee ID` AS EmployeeID, COUNT(*) AS No_Orders
  FROM `orders` o
  GROUP BY o.`Employee ID`
)
SELECT EmployeeID, No_Orders
FROM counts
WHERE No_Orders = (SELECT MAX(No_Orders) FROM counts);

-- 6. Show the last name of the employee having the highest number of orders
WITH counts AS (
  SELECT o.`Employee ID` AS EmployeeID, COUNT(*) AS No_Orders
  FROM `orders` o
  GROUP BY o.`Employee ID`
),
top_emp AS (
  SELECT EmployeeID
  FROM counts
  WHERE No_Orders = (SELECT MAX(No_Orders) FROM counts)
)
SELECT e.`Last Name`
FROM employees e
JOIN top_emp t ON t.EmployeeID = e.`ID`;

-- 7. Compute the subtotal of each Order ID where the subtotal is the sum of values of all the corresponding order lines. Note: the value of each line was mentioned in question 11 of Assignment 3, which is (Quantity * [Unit Price])*(1-Discount)
SELECT
  od.`Order ID` AS OrderID,
  SUM(od.`Quantity` * od.`Unit Price` * (1 - od.`Discount`)) AS Subtotal
FROM `order details` od
GROUP BY od.`Order ID`
ORDER BY OrderID;

-- 8. Show the Order ID(s) with a subtotal greater than 1500 in the descending order.
WITH sub AS (
  SELECT
    od.`Order ID` AS OrderID,
    SUM(od.`Quantity` * od.`Unit Price` * (1 - od.`Discount`)) AS Subtotal
  FROM `order details` od
  GROUP BY od.`Order ID`
)
SELECT OrderID, ROUND(Subtotal, 2) AS Subtotal
FROM sub
WHERE Subtotal > 1500
ORDER BY Subtotal DESC;

-- 9. Count how many orders each Employee ID have processed. If an Employee ID has no corresponding order, his results should be 0. A part of the results will look like the below figure.
SELECT
  e.`ID` AS EmployeeID,
  COALESCE(COUNT(o.`Order ID`), 0) AS No_Orders
FROM employees e
LEFT JOIN `orders` o ON o.`Employee ID` = e.`ID`
GROUP BY e.`ID`
ORDER BY EmployeeID;

-- 10. Compute the sale of each product. The results should consist of 3 columns: Product ID, Product Name, and Sale.
SELECT
  p.`ID`           AS ProductID,
  p.`Product Name` AS ProductName,
  SUM(od.`Quantity` * od.`Unit Price` * (1 - od.`Discount`)) AS Sale
FROM `order details` od
JOIN products p ON p.`ID` = od.`Product ID`
GROUP BY p.`ID`, p.`Product Name`
ORDER BY ProductID;

-- 11. Show products who List Price(s) are greater than the average List Price of all products in the table Products.
SELECT
  p.`Product Name`,
  p.`List Price`
FROM products p
WHERE p.`List Price` > (SELECT AVG(`List Price`) FROM products)
ORDER BY p.`Product Name`;

-- 12. Compute the average shipping fee to each city of orders with status “Closed”. The resulting rows consist of only average values greater than or equal to 100, and is sorted in ascending sequence.
SELECT
  o.`Ship City` AS City,
  AVG(o.`Shipping Fee`) AS AvgShipping
FROM `orders` o
JOIN `orders status` s ON s.`Status ID` = o.`Status ID`
WHERE s.`Status Name` = 'Closed'
GROUP BY o.`Ship City`
HAVING AVGShipping >= 100
ORDER BY AvgShipping ASC;

-- 13. Show products who List Price(s) are greater than the average List Price of all products in the same category. The results includes 4 columns: Product Name, List Price, Category, and AVG Price of Category
WITH cat_avg AS (
  SELECT
    p.`Category`,
    AVG(p.`List Price`) AS `Avg Price Of Category`
  FROM products p
  GROUP BY p.`Category`
)
SELECT
  p.`Product Name` AS `Product Name`,
  ROUND(p.`List Price`, 2) AS `List Price`,
  p.`Category` AS Category,
  ROUND(ca.`Avg Price Of Category`, 2) AS `AVG Price of Category`
FROM products p
JOIN cat_avg ca
  ON ca.`Category` = p.`Category`
WHERE p.`List Price` > ca.`Avg Price Of Category`
ORDER BY p.`Category`, p.`Product Name`;


-- 14. Compute how many days in average each Employer ID processes orders (from the Order Date to the Shipped Date). Note: only orders with Shipped Date filled are considered in this query.
SELECT
  o.`Employee ID` AS EmployeeID,
  AVG(DATEDIFF(o.`Shipped Date`, o.`Order Date`)) AS AvgDays
FROM `orders` o
WHERE o.`Shipped Date` IS NOT NULL
GROUP BY o.`Employee ID`
ORDER BY EmployeeID;

-- 15. Retrieve information of orders with the following columns: Customer’s Company, Employee’s Last Name, Order Date, and Order Status Name.
SELECT
  c.`Company`     AS `Customer Company`,
  e.`Last Name`   AS `Employee LastName`,
  o.`Order Date`  AS `Order Date`,
  s.`Status Name` AS `Order Status Name`
FROM `orders` o
JOIN customers      c ON c.`ID` = o.`Customer ID`
JOIN employees      e ON e.`ID` = o.`Employee ID`
JOIN `orders status` s ON s.`Status ID` = o.`Status ID`
ORDER BY o.`Order Date`, c.`Company`;