-- 11 April 2026 SQL Practice

SHOW DATABASES;
USE temp;
SHOW TABLES;

-- DESCRIBE table
DESC customer;

-- 1. Basic DML: INSERT, SELECT, UPDATE, DELETE
INSERT INTO customer(id, cname, address, cit, pincode) VALUES (1251, 'ram kumar', 'jalandhar', 'idk', 123);
SELECT * FROM customer;

UPDATE customer SET cit='lol' WHERE id='1251';
SELECT * FROM customer;

DELETE FROM customer WHERE id=1251;
SELECT * FROM customer;

-- Insert another record
INSERT INTO customer VALUES(1,'Ram kumar','Punjab','Jalandhar','12333');

DESC tables;
SELECT * FROM tables;
SELECT * FROM customer;

-- 2. Foreign Keys
-- Creating a table with a basic foreign key
CREATE TABLE Order_details (
    Order_id INT PRIMARY KEY,
    delivery_date DATE,
    cust_id INT,
    FOREIGN KEY (cust_id) REFERENCES customer(id)
);
INSERT INTO Order_details VALUES(1,'2019-03-11',1);
SELECT * FROM Order_details;

-- Trying to delete a parent row will fail here because of the child row
-- delete from customer where id=1;  -- ERROR 1451

DROP TABLE Order_details;

-- 3. ON DELETE CASCADE
CREATE TABLE Order_details(
    Order_id INT PRIMARY KEY,
    delivery_date DATE,
    cust_id INT,
    FOREIGN KEY(cust_id) REFERENCES customer(id) ON DELETE CASCADE
);

INSERT INTO Order_details VALUES(1,'2026-05-10',1);
INSERT INTO Order_details VALUES(4,'2026-05-11',1);

SELECT * FROM Order_details;

-- Deleting parent row now deletes child rows
DELETE FROM customer WHERE id=1;

SELECT * FROM customer;
SELECT * FROM Order_details;

DROP TABLE Order_details;

-- 4. ON DELETE SET NULL
CREATE TABLE Order_details(
    Order_id INT PRIMARY KEY,
    delivery_date DATE,
    cust_id INT,
    FOREIGN KEY(cust_id) REFERENCES customer(id) ON DELETE SET NULL
);

INSERT INTO customer VALUES(1,'Ram kumar','Punjab','Jalandhar','12333');
INSERT INTO Order_details VALUES(4,'2026-03-11',1);

-- Deleting parent row sets child's foreign key column to NULL
DELETE FROM customer WHERE id=1;

SELECT * FROM customer;
SELECT * FROM Order_details;

-- 5. REPLACE statement
-- Replaces if row exists (by Primary Key), otherwise Inserts new row
REPLACE INTO customer(id,cit) VALUES(1,'rohtak');
SELECT * FROM customer;

REPLACE INTO customer(id,cit) VALUES(12,'rohtak');
SELECT * FROM customer;
