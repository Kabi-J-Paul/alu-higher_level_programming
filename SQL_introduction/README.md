# SQL - Introduction

MySQL 8.0 scripts covering DDL and DML basics: creating and dropping
databases, creating tables, inserting, selecting, updating and deleting
rows, and using aggregate functions.

Scripts are run by piping them into the mysql client. Where a script works
on a specific database, that name is passed as the last argument.
## Files

| File | Description |
| --- | --- |
| 0-list databases.sql | Lists all databases on the server |
| 1-create database if missing.sql | Creates hbtn 0c 0 without failing if it exists |
| 2-remove database.sql | Drops hbtn 0c 0 without failing if it is missing |
| 3-list tables.sql | Lists the tables of the database passed as argument |
| 4-first table.sql | Creates the table first table |
| 5-full table.sql | Prints the full description of first table |
| 6-list values.sql | Lists all rows of first table |
| 7-insert value.sql | Inserts one row into first table |
| 8-count 89.sql | Counts the records with id = 89 |
| 9-full creation.sql | Creates second table and adds four records |
| 10-top score.sql | Lists all records, highest score first |
| 11-best score.sql | Lists records with a score of 10 or more |
| 12-no cheating.sql | Updates Bob's score to 10, by name |
| 13-change class.sql | Removes records with a score of 5 or less |
| 14-average.sql | Computes the average score |
| 15-groups.sql | Counts records per score |
| 16-no link.sql | Lists records that have a name | 
