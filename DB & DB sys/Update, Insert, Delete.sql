use qacs;

#1 Using INSERT and columns specified, add yourself to the CUSTOMER table. Explicitly list the columns you are adding and only the ones you need.
Select * from Customer;

Insert into Customer
values(null, 'Nguyen', 'Thanh', 'Vinuni', 'Hanoi', 'NA', 
'100000', '0968100710', 'nguyendatthanh0710@gmail.com');

#2 Using INSERT and columns specified, add one of your classmates to the EMPLOYEE table. Explicitly list the columns you are adding and only the ones you need.
Select * from Employee;
Insert into Employee
values(null, 'Tien', 'Hieu', '012345678', 'tmhlol@gmail.com');

#3 Suppose we want to write all the US cities in uppercase. Write a SQL statement to update all vendor cities (Column City in VENDOR table) and a SQL statement to update all customer cities (Column City in CUSTOMER table), so that they are uppercase.
Update Vendor
set City = ucase(City)
where VendorID > 0;

Select * from Vendor;

Update Customer
set City = ucase(City)
where CustomerID > 0;

select * from Customer;

#4 Question 1 asked you to add yourself to the CUSTOMER table. Now delete yourself. Make sure to use a WHERE clause, or you will delete all customers!
select * from Customer;

delete from Customer
where Address = 'Vinuni' and CustomerID > 50;

select * from Customer;

#5 Add a website column (namely, VendorWebsite) to the VENDOR table. You need a text field big enough to accommodate a URL (e.g., TEXT(100)).
Alter table Vendor
add column Website text(100);

select * from Vendor;
#6 Use UPDATE statements to update VENDOR records to include a website (you can make up any address). 
update Vendor
set Website = 'https://www.w3schools.com/sql/sql_count.asp'
where VendorID > 0;

select * from Vendor;