/*-------------------------------------------------------*/
use wp;
/* Correlated Subqueries */            
/* YOUR SQL STATEMENT HERE */
SELECT
  E1.EmployeeNumber,
  E1.FirstName,
  E1.LastName
FROM EMPLOYEE AS E1
WHERE E1.LastName IN (
  SELECT E2.LastName
  FROM EMPLOYEE AS E2
  WHERE E1.LastName = E2.LastName
    AND E1.EmployeeNumber <> E2.EmployeeNumber
);

/* Exists and Not Exists*/
/* YOUR SQL STATEMENT HERE */
SELECT
  E1.EmployeeNumber,
  E1.FirstName,
  E1.LastName
FROM EMPLOYEE AS E1
WHERE EXISTS (
  SELECT 1
  FROM EMPLOYEE AS E2
  WHERE E2.LastName = E1.LastName
    AND E2.EmployeeNumber <> E1.EmployeeNumber
);

/* Queries on Recursive Relationships */
/* YOUR SQL STATEMENT HERE */
SELECT
  S.FirstName AS SupervisorFirstName,
  S.LastName  AS SupervisorLastName,
  E.FirstName AS EmployeeFirstName,
  E.LastName  AS EmployeeLastName
FROM EMPLOYEE AS S
JOIN EMPLOYEE AS E
  ON S.EmployeeNumber = E.Supervisor
ORDER BY S.EmployeeNumber;


/* Set Operators */
SELECT SKU, CatalogDescription, CatalogPage, DateOnWebSite
FROM CATALOG_SKU_2017
UNION
SELECT SKU, CatalogDescription, CatalogPage, DateOnWebSite
FROM CATALOG_SKU_2018;

/* Create view */
/* YOUR SQL STATEMENT HERE */
CREATE VIEW BasicDepartmentDataView AS
SELECT DepartmentName, DepartmentPhone
FROM DEPARTMENT;


/* YOUR SQL STATEMENT HERE */
CREATE VIEW ProjectHoursToDateView AS
SELECT
  p.ProjectID,
  p.ProjectName,
  p.MaxHours AS ProjectMaxHours,
  SUM(a.HoursWorked) AS ProjectHoursWorkedToDate
FROM PROJECT AS p
JOIN ASSIGNMENT AS a
  ON p.ProjectID = a.ProjectID
GROUP BY p.ProjectID, p.ProjectName, p.MaxHours;

    
/* YOUR SQL STATEMENT HERE */
CREATE VIEW EmployeeProjectHoursWorkedView AS
SELECT
  p.ProjectName,
  e.FirstName,
  e.LastName,
  a.HoursWorked
FROM EMPLOYEE AS e
JOIN ASSIGNMENT AS a
  ON e.EmployeeNumber = a.EmployeeNumber
JOIN PROJECT AS p
  ON a.ProjectID = p.ProjectID
ORDER BY p.ProjectID, a.EmployeeNumber;


/* Layering Computations and Built-In Functions*/
/* YOUR SQL STATEMENT HERE */
CREATE OR REPLACE VIEW ProjectHoursToDateView AS
SELECT
  p.ProjectID,
  p.ProjectName,
  p.MaxHours AS ProjectMaxHours,
  COALESCE(SUM(a.HoursWorked), 0) AS ProjectHoursWorkedToDate
FROM PROJECT AS p
LEFT JOIN ASSIGNMENT AS a
  ON p.ProjectID = a.ProjectID
GROUP BY p.ProjectID, p.ProjectName, p.MaxHours;

SELECT ProjectID, ProjectName, ProjectMaxHours, ProjectHoursWorkedToDate
FROM ProjectHoursToDateView
WHERE ProjectHoursWorkedToDate > ProjectMaxHours
ORDER BY ProjectID;

/* YOUR SQL STATEMENT HERE */
CREATE OR REPLACE VIEW ProjectsOverAllocatedMaxHoursView AS
SELECT ProjectID, ProjectName, ProjectMaxHours, ProjectHoursWorkedToDate
FROM ProjectHoursToDateView
WHERE ProjectHoursWorkedToDate > ProjectMaxHours;

SELECT
  ProjectID,
  ProjectName,
  ProjectMaxHours,
  ProjectHoursWorkedToDate,
  (ProjectHoursWorkedToDate - ProjectMaxHours) AS HoursOverMaxAllocated
FROM ProjectsOverAllocatedMaxHoursView
ORDER BY ProjectID;

/* YOUR SQL STATEMENT HERE */



DELIMITER $$

CREATE FUNCTION NameConcatenation(
    FirstName CHAR(25),
    LastName  CHAR(25)
)
RETURNS VARCHAR(60)
DETERMINISTIC
BEGIN
    -- you can return directly without a local var
    RETURN CONCAT(LastName, ', ', FirstName);
END$$

DELIMITER ;

delimiter $$

-- 1. Capitalize vowels
DROP FUNCTION IF EXISTS capitalize_vowels;
CREATE FUNCTION capitalize_vowels(s TEXT)
RETURNS TEXT
DETERMINISTIC
RETURN REPLACE(
         REPLACE(
           REPLACE(
             REPLACE(
               REPLACE(s,'a','A'),
             'e','E'),
           'i','I'),
         'o','O'),
       'u','U');

-- 2) Convert date to dd/mm/yyyy
CREATE FUNCTION to_ddmmyyyy(d DATE)
RETURNS VARCHAR(10)
DETERMINISTIC
RETURN DATE_FORMAT(d, '%d/%m/%Y');
DROP FUNCTION IF EXISTS to_ddmmyyyy_str;
CREATE FUNCTION to_ddmmyyyy_str(dstr VARCHAR(20))
RETURNS VARCHAR(10)
DETERMINISTIC
RETURN DATE_FORMAT(STR_TO_DATE(dstr, '%Y-%m-%d'), '%d/%m/%Y');

DELIMITER $$

-- Trigger 

ALTER TABLE EMPLOYEE
  ADD COLUMN Apprenticeship VARCHAR(20);

ALTER TABLE EMPLOYEE
  ADD CONSTRAINT Required
  CHECK (Apprenticeship IN ('Completed', 'In process', 'Not started'));


CREATE TRIGGER upd_check
BEFORE UPDATE ON EMPLOYEE
FOR EACH ROW
BEGIN
  
  IF NEW.Apprenticeship IS NOT NULL THEN
    CASE
      WHEN LOWER(NEW.Apprenticeship) LIKE '%completed%'    THEN SET NEW.Apprenticeship = 'Completed';
      WHEN LOWER(NEW.Apprenticeship) LIKE '%in process%'   THEN SET NEW.Apprenticeship = 'In process';
      WHEN LOWER(NEW.Apprenticeship) LIKE '%not started%'  THEN SET NEW.Apprenticeship = 'Not started';
      
    END CASE;
  END IF;
END$$

DELIMITER ;

UPDATE EMPLOYEE
SET Apprenticeship = CASE EmployeeID
  WHEN 1 THEN 'Completed.  '
  WHEN 2 THEN '4In processasd'
  WHEN 3 THEN '3Not started'
  WHEN 4 THEN 'asdCompleted'
  WHEN 5 THEN 'In processedd'
  ELSE Apprenticeship
END;


-- Store Procedure

DELIMITER $$

CREATE PROCEDURE SaleReport(IN eid INT)

BEGIN
  SELECT
    COALESCE(SUM(Total), 0) AS `Total Sales made`
  FROM qacs.SALE
  WHERE EmployeeID = eid;   -- (using = instead of IN (eid))
END$$

DELIMITER ;

CALL SaleReport(1);
CALL SaleReport(0);
CALL SaleReport('1');
CALL SaleReport(1, 2);




