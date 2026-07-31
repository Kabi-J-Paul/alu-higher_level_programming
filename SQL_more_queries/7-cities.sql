-- Creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switches to the newly created database
USE hbtn_0d_usa;
-- Creates cities with state_id referencing the states table
CREATE TABLE IF NOT EXISTS cities (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id)
);
