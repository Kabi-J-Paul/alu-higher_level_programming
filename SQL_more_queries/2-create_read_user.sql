-- Creates the database hbtn_0d_2 and a read-only user for it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the user user_0d_2 without failing if it already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT only, and only on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
