USE qacs;
/*P1*/
SELECT ItemID, ItemDescription, ItemCost, ItemPrice
FROM ITEM;

SELECT DISTINCT ItemDescription
FROM ITEM;

SELECT EmailAddress, LastName, FirstName
FROM EMPLOYEE;

SELECT EmailAddress
FROM VENDOR
WHERE EmailAddress IS NOT NULL;

SELECT SaleID, CustomerID, EmployeeID
FROM SALE;

SELECT DISTINCT SaleDate
FROM SALE
ORDER BY SaleDate;

/*P2*/
SELECT FirstName
FROM CUSTOMER
ORDER BY FirstName ASC;

SELECT *
FROM CUSTOMER
ORDER BY FirstName ASC;

SELECT LastName
FROM CUSTOMER
ORDER BY FirstName ASC;

SELECT *
FROM CUSTOMER
ORDER BY Address ASC, City ASC, ZIP ASC;

SELECT *
FROM ITEM
ORDER BY ItemPrice DESC;

SELECT ItemDescription
FROM ITEM
ORDER BY ItemPrice DESC
LIMIT 5;

SELECT *
FROM CUSTOMER
WHERE City = 'Bellevue';

SELECT *
FROM ITEM
WHERE ItemPrice > 500;

SELECT *
FROM VENDOR
WHERE CompanyName <> 'European Specialties' OR CompanyName IS NULL;

SELECT *
FROM SALE
WHERE SaleDate < '2019-01-05';

SELECT *
FROM ITEM
WHERE ItemDescription LIKE 'Dining Table%';

SELECT *
FROM VENDOR
WHERE ContactLastName = 'Nelson'
   OR ContactFirstName = 'Andrew';

SELECT *
FROM CUSTOMER
WHERE Address LIKE '%Aloha%';


