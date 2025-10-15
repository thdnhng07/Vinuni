use wp;

# Adding ApprovalDate Column to PRODUCTION_ITEM
/* YOUR SQL STATEMENT HERE */
alter table PRODUCTION_ITEM
add ApprovalDate Date;

-- Run the following SELECT statement to see the added ApprovalDate column   
SELECT * FROM PRODUCTION_ITEM;    

/* *** SQL-UPDATE-ExtB-01 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2016-08-31'
	WHERE SKU = 170102001;
/* *** SQL-UPDATE-ExtB-02 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2016-08-31'
	WHERE SKU = 170102005;
/* *** SQL-UPDATE-ExtB-03 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2016-09-30'
	WHERE SKU = 170201001;
/* *** SQL-UPDATE-ExtB-04 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2016-09-30'
	WHERE SKU = 170201005;
/* *** SQL-UPDATE-ExtB-05 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2016-11-30'
	WHERE SKU = 170303001;
/* *** SQL-UPDATE-ExtB-06 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2016-11-30'
	WHERE SKU = 170303005;
/* *** SQL-UPDATE-ExtB-07 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2017-09-30'
	WHERE SKU = 180103001;
/* *** SQL-UPDATE-ExtB-08 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2017-09-30'
	WHERE SKU = 180103005;
/* *** SQL-UPDATE-ExtB-09 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2017-09-30'
	WHERE SKU = 180202001;
/* *** SQL-UPDATE-ExtB-10 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2017-09-30'
	WHERE SKU = 180202005;
/* *** SQL-UPDATE-ExtB-11 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2017-11-30'
	WHERE SKU = 180304001;
/* *** SQL-UPDATE-ExtB-12 *** */
UPDATE PRODUCTION_ITEM
	SET ApprovalDate = '2017-11-30'
	WHERE SKU = 180304005;
    
/* Modify the column to add Not Null constraint */
/* YOUR SQL STATEMENT HERE */
alter table PRODUCTION_ITEM
modify ApprovalDate DATE not null;

/* Adding ApprovalDate < ProductionStartDate Constraint to  PRODUCTION_ITEM table*/
/* YOUR SQL STATEMENT HERE */
alter table production_item
add constraint check(ApprovalDate < ProductionStartDate);

/* Test query */
INSERT INTO PRODUCTION_ITEM VALUES( 
180304007,'Bravo I+, Black', '2016-12-15', '2017-11-30', 0, 0, '2016-12-16'); 


/* Drop the Constraint of an Existing Table*/
/* YOUR SQL STATEMENT HERE */
alter table production_item
drop constraint production_item_chk_3;

/* Drop a Table column from an existing table*/
/* YOUR SQL STATEMENT HERE */
alter table production_item
drop column ApprovalDate;
    
-- ALTER TABLE CATALOG_SKU_2018
-- 	DROP PRIMARY KEY;
alter table CATALOG_SKU_2018
drop Primary KEY;

/* Adding new Referential Integrity Constraint*/
/* YOUR SQL STATEMENT HERE */
alter table CATALOG_SKU_2018
	add constraint CAT18_PROD_ITEM_SK foreign key(SKU)
		references production_item(SKU)
        on update no action
        on delete no action;

/* Create the PRODUCTION_ ITEM_DATA Table */
CREATE TABLE PRODUCTION_ITEM_DATA(
	SKU 							Int 						NOT NULL,
	SKU_Description 				Char(35) 				NULL,
	ProductionStartDate 			Date 					NULL,
	ProductionEndDate 				Date 					NULL,
	QuantityOnHand 				Int 						NULL,
	QuantityInProduction 			Int 						NULL,
	ApprovalDate 					Date 					NULL,
	CONSTRAINT 				PROD_ITEM_PK 			PRIMARY KEY(SKU)
);

/*Adding Data to the  PRODUCTION_ITEM_ DATA Table*/
INSERT INTO PRODUCTION_ITEM_DATA(SKU, ProductionEndDate)
	VALUES(180103001, '31-10-18');
INSERT INTO PRODUCTION_ITEM_DATA(SKU, ProductionEndDate)
	VALUES(180103005, '31-10-18');
INSERT INTO PRODUCTION_ITEM_DATA 
	VALUES(190104001, 'Alpha IV, Black', '15-11-18', NULL, 0, 200, '15-10-18');
INSERT INTO PRODUCTION_ITEM_DATA 
	VALUES(190104005, 'Alpha IV, White', '15-11-18', NULL, 0, 200, '15-10-18');

alter table PRODUCTION_ITEM_DATA
drop ApprovalDate;

/* Merge Table in SQL Server*/
/* MERGE INTO PRODUCTION_ITEM AS PROI USING PRODUCTION_ITEM_DATA AS PROID
	ON PROI.SKU = PROID.SKU
	WHEN MATCHED THEN
		UPDATE SET PROI.ProductionEndDate = PROID.ProductionEndDate
	WHEN NOT MATCHED THEN
		INSERT (SKU, SKU_Description,
			ProductionStartDate, ProductionEndDate,
			QuantityOnHand, QuantityInProduction,
			ApprovalDate)
		    VALUES (PROID.SKU, PROID.SKU_Description,
			PROID.ProductionStartDate, PROID.ProductionEndDate,
			PROID.QuantityOnHand, PROID.QuantityInProduction,
			PROID.ApprovalDate);*/

Select * FROM PRODUCTION_ITEM;

INSERT INTO PRODUCTION_ITEM VALUES( 
190104001, 'Alpha IV, Black', '2018-11-15', NULL, 50, 200, '2018-10-15'); 
INSERT INTO PRODUCTION_ITEM VALUES( 
190104005, 'Alpha IV, White', '2018-11-15', NULL, 50, 200, '2018-10-15'); 
INSERT INTO PRODUCTION_ITEM VALUES( 
190203001, 'Bravo III, Black', '2018-12-15', NULL, 100, 250, '2018-11-15'); 
INSERT INTO PRODUCTION_ITEM VALUES( 
190203005, 'Bravo III, White', '2018-12-15', NULL, 100, 250, '2018-11-15'); 

/* Merge Table in MySQL*/
UPDATE PRODUCTION_ITEM
	SET ProductionEndDate = '2018-10-15'
	WHERE SKU = 190104001;

UPDATE PRODUCTION_ITEM
	SET ProductionEndDate = '2018-10-15'
	WHERE SKU = 190104005;
    
INSERT INTO PRODUCTION_ITEM VALUES(
	190203001, 'Alpha IV, Black', '2018-11-15', NULL, 0, 200, '2018-10-15');
 
INSERT INTO PRODUCTION_ITEM VALUES(
	190203005, 'Alpha IV, White', '2018-11-15', NULL, 0, 200, '2018-10-15');



/*-------------------------------------------------------*/
/* Correlated Subqueries */            
/* YOUR SQL STATEMENT HERE */

/* Exists and Not Exists*/
/* YOUR SQL STATEMENT HERE */

/* Queries on Recursive Relationships */
/* YOUR SQL STATEMENT HERE */

/* Set Operators */
SELECT SKU, CatalogDescription, CatalogPage, DateOnWebSite
FROM CATALOG_SKU_2017
UNION
SELECT SKU, CatalogDescription, CatalogPage, DateOnWebSite
FROM CATALOG_SKU_2018;

/* Create view */
/* YOUR SQL STATEMENT HERE */

/* YOUR SQL STATEMENT HERE */
    
/* YOUR SQL STATEMENT HERE */

/* Layering Computations and Built-In Functions*/
/* YOUR SQL STATEMENT HERE */

/* YOUR SQL STATEMENT HERE */

/* YOUR SQL STATEMENT HERE */




