-- This is a script that creates a table regardless of the DB and adds enums
CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country ENUM('US', 'CO', 'TN') DEFAULT 'US',
PRIMARY KEY(id)
); 
