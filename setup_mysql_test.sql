-- Create a database named hbnb_test_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user named hbnb_test with the password hbnb_test_pwd if the user doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY '13684146@Weldehiet';

-- Grant all privileges on the hbnb_test_db database to the hbnb_test user
-- This allows the user to perform all actions on the specified database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_test user
-- This allows the user to perform SELECT queries on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
