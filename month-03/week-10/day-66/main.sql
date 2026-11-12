-- CREATE TABLE, INSERT, and SELECT

psql -d book_api

SELECT current_database();

-- Create our first table
CREATE TABLE authors (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Insert values
INSERT INTO authors(name)
VALUES
    ('Gabriel Garcia Marquez'),
    ('George Orwell'),
    ('J. K. Rowling');

-- Check values
SELECT * FROM authors;

-- Consult specific columns
SELECT id, name FROM authors;

-- To filter
SELECT * FROM authors
WHERE name = 'George Orwell';

-- To order
SELECT * FROM authors
ORDER BY name ASC;

-- PRACTICE
CREATE TABLE books (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    published_year INTEGER
);

-- Check if table created
\dt

-- Insert values into books
INSERT INTO books (title, price, published_year) VALUES ('Clean Code', 35.99, 2008), ('Python Crash Course', 29.99, 2019), ('The pragmatic programmer', 40.50, 1999);
