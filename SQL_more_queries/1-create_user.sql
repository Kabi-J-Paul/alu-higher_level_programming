-- Creates the user user_0d_1 with all privileges on the server
-- Does not fail if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants every privilege on every database and table
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
