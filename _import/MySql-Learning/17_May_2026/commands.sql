-- Database creation and selection
CREATE DATABASE sql_practice_17_05_2026;
USE sql_practice_17_05_2026;
USE joins;
SHOW TABLES;
SHOW CREATE TABLE client;
SHOW DATABASES;

-- Using movie database
USE movie;
SHOW TABLES;
SHOW CREATE TABLE director;
SELECT * FROM director;
SHOW CREATE TABLE director_name;
SHOW CREATE TABLE movie;

-- Modifying constraints on director_name
ALTER TABLE director_name DROP FOREIGN KEY director_name_ibfk_1;

-- Updating director_name rows conditionally using CASE WHEN
UPDATE director_name
SET director_id = CASE
    WHEN director_name_id = 1231 THEN 1
    WHEN director_name_id = 1232 THEN 2
END
WHERE director_name_id IN (1231, 1232);

-- Adding a named foreign key constraint
ALTER TABLE director_name ADD CONSTRAINT fk FOREIGN KEY (director_id) REFERENCES movie(movie_id);

-- Modifying constraints and columns on director table
ALTER TABLE director DROP FOREIGN KEY director_ibfk_1;
ALTER TABLE director DROP COLUMN movie_id;
ALTER TABLE director ADD COLUMN name_id int not null;

-- Updating director rows conditionally using CASE WHEN
UPDATE director
SET name_id = CASE
    WHEN director_id = 1101 THEN 1231
    WHEN director_id = 1102 THEN 1232
END
WHERE director_id IN (1101, 1102);

-- Adding a named foreign key constraint linking to director_name
ALTER TABLE director ADD CONSTRAINT f_k FOREIGN KEY (name_id) REFERENCES director_name(director_name_id);

-- Joining 3 tables using the newly established foreign key relationships
SELECT m.movie_name, d.director_name, n.director_id 
FROM movie AS m 
JOIN director_name AS d ON d.director_id = m.movie_id 
JOIN director AS n ON n.name_id = d.director_name_id;
