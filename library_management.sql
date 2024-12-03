-- Create the database
CREATE DATABASE LibraryManagement;

-- Use the database
USE LibraryManagement;

-- Create table for books/movies
CREATE TABLE Items (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Type ENUM('Book', 'Movie') DEFAULT 'Book',
    AuthorOrDirector VARCHAR(255) NOT NULL,
    Year INT NOT NULL
);

-- Create table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    UserType ENUM('New', 'Existing') DEFAULT 'New'
);

-- Insert sample data into Items table
INSERT INTO Items (Name, Type, AuthorOrDirector, Year)
VALUES
('The Great Gatsby', 'Book', 'F. Scott Fitzgerald', 1925),
('Inception', 'Movie', 'Christopher Nolan', 2010);

-- Insert sample data into Users table
INSERT INTO Users (Name, UserType)
VALUES
('Alice', 'New'),
('Bob', 'Existing');

-- Query to fetch all books/movies
SELECT * FROM Items;

-- Query to fetch all users
SELECT * FROM Users;
-- Create the database
CREATE DATABASE LibraryManagement;

-- Use the database
USE LibraryManagement;

-- Create table for books/movies
CREATE TABLE Items (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Type ENUM('Book', 'Movie') DEFAULT 'Book',
    AuthorOrDirector VARCHAR(255) NOT NULL,
    Year INT NOT NULL
);

-- Create table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    UserType ENUM('New', 'Existing') DEFAULT 'New'
);

-- Insert sample data into Items table
INSERT INTO Items (Name, Type, AuthorOrDirector, Year)
VALUES
('The Great Gatsby', 'Book', 'F. Scott Fitzgerald', 1925),
('Inception', 'Movie', 'Christopher Nolan', 2010);

-- Insert sample data into Users table
INSERT INTO Users (Name, UserType)
VALUES
('Alice', 'New'),
('Bob', 'Existing');

-- Query to fetch all books/movies
SELECT * FROM Items;

-- Query to fetch all users
SELECT * FROM Users;
