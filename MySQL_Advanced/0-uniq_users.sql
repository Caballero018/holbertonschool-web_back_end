-- Script that creates a table users
CREATE TABLE users IF NOT EXISTS (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    );
