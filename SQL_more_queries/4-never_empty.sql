-- Creates the table id_not_null where id defaults to 1
CREATE TABLE IF NOT EXISTS id_not_null (
id INT NOT NULL DEFAULT 1,
name VARCHAR(256)
);
