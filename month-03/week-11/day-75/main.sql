-- INNER JOIN and LEFT JOIN

INSERT INTO authors(name)
VALUES ('Robert C. Martin'),
       ('Eric Matthes'),
       ('Andrew Hunt');


SELECT *
FROM authors;


ALTER TABLE books book_api ADD COLUMN author_id INTEGER;

-- PRACTICE

SELECT authors.name book_api->
FROM authors book_api->
LEFT JOIN books book_api-> ON authors.id = books.author_id book_api->
WHERE books.author_id IS NULL;