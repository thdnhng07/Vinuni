use Northwind;

-- 1.	(1 point) Return the list of customers (Last Name, First Name, Job Title), sort them by Last Name, then First Name, both by descending order.
select * from customers;

select
	`Last Name`,
  `First Name`,
  `Job Title`
from customers c
order by
  `Last Name` desc,
  `First Name` desc;

			
-- 2.	(1 point) How many distinct countries/regions has each employee shipped orders to? 
select * from `orders`;

select o.`Employee ID`, count(distinct o.`Ship Country/Region`) from orders o
group by o.`Employee ID`;

-- 3.	(1 point) Retrieve the average discount applied to orders shipped to USA.
select * from orders, `order details`;

select 
	o.`Ship Country/Region`,
	avg(od.Discount)
from orders o, `order details` od
group by o.`Ship Country/Region`;

-- 4.	(1 point) Return the State/Province with only one customer and the customer details (First Name, Last Name) in those states.
select * from customers;

with state_counts AS (
  select
    `State/Province`,
    count(*) as cnt
  from customers
  where `State/Province` is not null
  group by `State/Province`
)
select
  c.`State/Province`,
  c.`First Name`,
  c.`Last Name`
from Customers c
join state_counts sc
  on sc.`State/Province` = c.`State/Province`
where sc.cnt = 1
order by c.`State/Province`;

-- 5.	(1 point) You need to retrieve unique product categories in the Northwind Database. Which query is better? Explain why. 
SELECT DISTINCT Category FROM Products;

#better flow
-- 6.	(2 points) Retrieve (all columns) 3 orders which have the 6th, 7th, and 8th highest shipping fee.
select * from `orders`;

-- 7.	(1 point) Retrieves the employee who processed the highest number of orders across all months combined in 2006.
select
  e.`Employee ID`,
  e.`First Name`,
  e.`Last Name`,
  COUNT(*) AS `Orders Processed`
from orders o
join employees e on e.`Employee ID` = o.`Employee ID`
where o.`Order Date` >= date '2006-01-01'
  and o.`Order Date` <  date '2007-01-01'
group by e.`Employee ID`, e.`First Name`, e.`Last Name`
order by `Orders Processed` desc
fetch first 1 row only;

-- 8.	(1 point) Which employees have never processed an order for a customer from the same city they are based in?

-- 9.	(1 point) Consider the following query, when you want to get some information 

-- 10.	(1 point) You need to retrieve the top 10 most expensive products in the Northwind Database. Which query is better? Explain why. 

-- 11.	(1 point) Return all the Product Code, Product Name, Category, List Price, Standard Cost and Profit Margin (which can be computed as (List Price - Standard Cost)/ Standard Cost) of products, with Profit Margin larger or equal to 50%. The table products should contain all the needed information for this query.
