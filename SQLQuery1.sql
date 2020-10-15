create table Salesman (
salesman_id char(6), 
sales_name char(15), 
city char(20),
commission decimal(2,2))

Insert Into Salesman values('5001', 'James Hoog', 'New York', 0.15)
Insert Into Salesman values('5002 ', 'Nail Knite', 'Paris', 0.13)
Insert Into Salesman values('5005 ', 'Graham Zusi', 'london', 0.11)
Insert Into Salesman values('5006 ', 'Mc Lyon','Paris', 0.14)
Insert Into Salesman values('5007 ', 'Paul Adam ','Rome ', 0.13)
Insert Into Salesman values('5003 ', 'Geoff Cameron ','San Jose ', 0.12)
Select * from Salesman;

create table Customer (
customer_id char(6),
cust_name char(30),  
city char(30),      
grade decimal(6),    
sales_id char(6))

Insert Into Customer values('3002','Nick Rimando', 'New York' ,100,'5001')
Insert Into Customer values('3007','Brad Davis  ', 'Newyork' , 200,'5002')
Insert Into Customer values('3005','Graham Zusi', 'California' ,200,'5005')
Insert Into Customer values('3008','Julian Green', 'London' ,300, '5006')
Insert Into Customer values('3004','Fabian Johnson', 'Paris' ,300, '5005')
Insert Into Customer values('3009','Geoff Cameron', 'Berlin' ,100, '5005')
Insert Into Customer values('3003','Jozy Altidor', 'Moscow' ,200, '5003')
Insert Into Customer values('3001','Brad Guzan',  'London' , 0  ,  '5002')
Select * from Customer;

/*1.Write a query to display all salesmen and customers located in London.*/

SELECT cust_name "Salesmen & Customer in London" FROM Customer
WHERE  city='London'
UNION
SELECT sales_name FROM salesman
WHERE  city='London'
/*2.Write a query to display all the customer names who all are salesmen also.*/

SELECT salesman.sales_name "Salesmen who are also Customer"
FROM Salesman,Customer
WHERE Salesman.sales_name=Customer.cust_name

/*3.Write a query to change the grade column of Customer table to 500 where Customer_id is 3008.*/
Select Customer.Grade, Customer_id from Customer /* Before Change*/
WHERE Customer_id = 3008
UPDATE Customer
SET Grade = 500
WHERE Customer_id = 3008
Select Customer.Grade, Customer_id from Customer /* After Change*/
WHERE Customer_id = 3008


/*4.Write a query to display distinct salesmen and their cities.*/

SELECT DISTINCT  salesman.sales_name,salesman.city FROM salesman;

/*5.Write a query to update the customer name to “Hilton” whose ID is 3007.*/
Select cust_name,customer_id from Customer 
WHERE  customer_id=3007
UPDATE Customer
SET cust_name = 'Hilton'
WHERE  customer_id=3007
Select cust_name,customer_id from Customer
WHERE  customer_id=3007

/*6.Write a query to display all the customers who are not salesman.*/

Select cust_name "All the customers who are not salesmen"
from customer
Except
Select sales_name
from salesman

/*7.Write a query to add column named country in Salesman table.*/

ALTER TABLE salesman
ADD country char(20); 
Select * from Salesman

/*8.Write a query to delete a column named country from the salesman table.*/
ALTER TABLE salesman
DROP COLUMN country
Select * from Salesman

/*9.Write a query to change the grade column data types as smallint.*/
ALTER TABLE customer
ALTER COLUMN grade smallint;

/*10.Write a query to delete data from Customer table where ID is 3001.*/
select Customer.customer_id from customer WHERE customer_id= 3001
DELETE FROM Customer WHERE customer_id= 3001; 
select*  from Customer 